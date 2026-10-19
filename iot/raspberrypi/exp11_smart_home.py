"""
Experiment 11: Smart Home using IoT (Raspberry Pi + Python + Flask)

What it does
  1. When a person enters the house (PIR / IR entry sensor triggers), the appliances set for the
     ACTIVE PERSON (profile) are switched ON automatically (e.g. Father: light + fan, Guest: light only).
  2. All appliances can also be controlled remotely from a web page on the same Wi-Fi network.

Wiring (BCM numbers; use a 2-channel relay module, relay IN pins to the GPIOs below)
  PIR / entry sensor OUT -> GPIO4 (pin 7)      PIR VCC -> 5V, GND -> GND
  Relay 1 (LIGHT)        -> GPIO17 (pin 11)
  Relay 2 (FAN)          -> GPIO27 (pin 13)
  Relay VCC -> 5V, GND -> GND. Mains appliances go through the relay contacts - ask your lab
  instructor before wiring anything above 12 V; for the demo use LEDs / a small DC fan.

Setup and run
  sudo apt install python3-flask        (or: pip3 install flask)
  python3 exp11_smart_home.py
  Open  http://<raspberry-pi-ip>:5000   from a phone or PC (find the IP with:  hostname -I)

If RPi.GPIO is not installed (e.g. you test on a laptop) the program runs in SIMULATION mode,
and the web page still works - handy for practising.
"""
import threading
import time

from flask import Flask, jsonify, redirect, render_template_string, request, url_for

# ---------------------------------------------------------------- GPIO (real or simulated)
try:
    import RPi.GPIO as GPIO
    SIMULATION = False
except ImportError:
    SIMULATION = True

    class _FakeGPIO:                        # minimal stand-in so the code runs anywhere
        BCM, OUT, IN, HIGH, LOW = "BCM", "OUT", "IN", 1, 0
        def setwarnings(self, *_): pass
        def setmode(self, *_): pass
        def setup(self, *_, **__): pass
        def output(self, pin, value): print(f"[sim] GPIO{pin} -> {value}")
        def input(self, pin): return 0
        def cleanup(self): pass
    GPIO = _FakeGPIO()

PIR_PIN = 4
PINS = {"light": 17, "fan": 27}
RELAY_ACTIVE_LOW = True                      # most relay boards switch ON when the pin goes LOW

# Appliances to switch ON when each person enters
PROFILES = {
    "Father": {"light": True, "fan": True},
    "Mother": {"light": True, "fan": False},
    "Guest":  {"light": True, "fan": False},
    "Child":  {"light": False, "fan": True},
}
AUTO_OFF_SECONDS = 0                         # 0 = never switch off automatically

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
for pin in PINS.values():
    GPIO.setup(pin, GPIO.OUT)

state = {"light": False, "fan": False, "person": "Father", "last_event": "System started"}
lock = threading.Lock()
last_motion = 0.0


def drive(appliance, on):
    """Switch one appliance and remember its state."""
    level = (not on) if RELAY_ACTIVE_LOW else on
    GPIO.output(PINS[appliance], GPIO.HIGH if level else GPIO.LOW)
    state[appliance] = bool(on)


for a in PINS:                               # start with everything OFF
    drive(a, False)


def entry_monitor():
    """Background thread: when the entry sensor triggers, apply the active person's profile."""
    global last_motion
    previous = 0
    while True:
        current = GPIO.input(PIR_PIN)
        with lock:
            if current and not previous:     # rising edge = someone entered
                profile = PROFILES[state["person"]]
                for appliance, on in profile.items():
                    if on:
                        drive(appliance, True)
                state["last_event"] = f"{state['person']} entered - profile applied ({time.strftime('%H:%M:%S')})"
                last_motion = time.time()
            if AUTO_OFF_SECONDS and last_motion and time.time() - last_motion > AUTO_OFF_SECONDS:
                for appliance in PINS:
                    drive(appliance, False)
                last_motion = 0.0
        previous = current
        time.sleep(0.2)


threading.Thread(target=entry_monitor, daemon=True).start()

# ---------------------------------------------------------------- Web interface
app = Flask(__name__)

PAGE = """
<!doctype html><html><head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Smart Home</title>
<style>
 body{font-family:Arial,sans-serif;max-width:480px;margin:20px auto;padding:0 14px}
 .card{border:1px solid #ccc;border-radius:12px;padding:14px;margin:12px 0}
 .row{display:flex;justify-content:space-between;align-items:center}
 .on{color:#0a7d2c;font-weight:bold}.off{color:#b00020;font-weight:bold}
 button,select{font-size:16px;padding:8px 14px;border-radius:8px;border:1px solid #888}
 .sim{background:#fff3cd;padding:6px 10px;border-radius:8px}
</style></head><body>
<h2>Smart Home Control</h2>
{% if sim %}<p class="sim">Simulation mode (no GPIO found)</p>{% endif %}
<div class="card">
  {% for name in appliances %}
  <div class="row" style="margin:8px 0">
    <span>{{ name|capitalize }}: <span class="{{ 'on' if state[name] else 'off' }}">{{ 'ON' if state[name] else 'OFF' }}</span></span>
    <form method="post" action="{{ url_for('toggle', appliance=name) }}"><button>Turn {{ 'OFF' if state[name] else 'ON' }}</button></form>
  </div>
  {% endfor %}
  <form method="post" action="{{ url_for('all_off') }}"><button>All OFF</button></form>
</div>
<div class="card">
  <form method="post" action="{{ url_for('set_person') }}">
    <label>Person at home / entering:</label><br><br>
    <select name="person">
      {% for p in profiles %}<option {{ 'selected' if p==state.person }}>{{ p }}</option>{% endfor %}
    </select>
    <button>Set</button>
  </form>
  <p>Profile: {% for a,on in profiles[state.person].items() %}{{ a }}={{ 'ON' if on else 'off' }} {% endfor %}</p>
</div>
<div class="card"><b>Last event:</b> {{ state.last_event }}</div>
<script>setTimeout(()=>location.reload(), 5000)</script>
</body></html>
"""


@app.route("/")
def index():
    return render_template_string(PAGE, state=state, appliances=list(PINS), profiles=PROFILES, sim=SIMULATION)


@app.route("/toggle/<appliance>", methods=["POST"])
def toggle(appliance):
    if appliance in PINS:
        with lock:
            drive(appliance, not state[appliance])
            state["last_event"] = f"{appliance} switched {'ON' if state[appliance] else 'OFF'} from web ({time.strftime('%H:%M:%S')})"
    return redirect(url_for("index"))


@app.route("/all_off", methods=["POST"])
def all_off():
    with lock:
        for a in PINS:
            drive(a, False)
        state["last_event"] = f"All appliances OFF from web ({time.strftime('%H:%M:%S')})"
    return redirect(url_for("index"))


@app.route("/person", methods=["POST"])
def set_person():
    person = request.form.get("person")
    if person in PROFILES:
        with lock:
            state["person"] = person
            state["last_event"] = f"Active person set to {person}"
    return redirect(url_for("index"))


@app.route("/status")                       # JSON status - also handy for demos / other apps
def status():
    return jsonify({k: state[k] for k in ("light", "fan", "person", "last_event")})


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()
