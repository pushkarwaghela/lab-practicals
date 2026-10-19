"""
Experiment 9: Raspberry Pi with HC-SR04 ultrasonic sensor - measure distance
Wiring:  VCC  -> 5V (pin 2)            GND -> GND (pin 6)
         TRIG -> GPIO23 (pin 16)
         ECHO -> GPIO24 (pin 18) through a level shifter or a voltage divider (1K in series, 2K to GND):
                 ECHO outputs 5 V but Pi GPIO pins are 3.3 V only.
Formula: distance = (time taken x speed of sound) / 2      speed of sound = 34300 cm/s
         equivalently distance(cm) = echo pulse width (us) / 58
Run:     python3 exp09_ultrasonic_distance.py          (Ctrl+C to stop)
"""
import time
import RPi.GPIO as GPIO

TRIG = 23
ECHO = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
print("Waiting for sensor to settle...")
time.sleep(2)


def measure_distance():
    GPIO.output(TRIG, True)            # 10 microsecond trigger pulse
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout = time.time() + 0.1        # avoid waiting forever if nothing is connected
    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            return None
    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            return None

    pulse_duration = pulse_end - pulse_start          # seconds
    return round(pulse_duration * 34300 / 2, 2)       # cm


try:
    while True:
        d = measure_distance()
        if d is None:
            print("No echo received - check wiring")
        else:
            print(f"Distance: {d} cm   ({round(d / 2.54, 2)} inch)")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    GPIO.cleanup()
