"""
Experiment 8: Raspberry Pi GPIO - LED connected to a GPIO pin, blink it
Wiring: GPIO25 (physical pin 22) -> 1 kOhm resistor -> LED anode ; LED cathode -> GND (pin 20 or 6)
Run:    python3 exp08_gpio_led_blink.py          (Ctrl+C to stop)

GPIO numbering: GPIO.BCM uses the Broadcom number (GPIO25); GPIO.BOARD uses the physical pin number (22).
Raspberry Pi 5: RPi.GPIO does not work on Pi 5. Run once:  pip uninstall RPi.GPIO ; pip install rpi-lgpio
(or use the gpiozero version at the bottom of this file).
"""
import time
import RPi.GPIO as GPIO

LED_PIN = 25                      # BCM numbering

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)            # use GPIO.BOARD for physical pin numbers
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)             # change the delay and observe the output
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    GPIO.cleanup()


# ---- Alternative using gpiozero (works on every Raspberry Pi model) ----
# from gpiozero import LED
# from time import sleep
# led = LED(25)
# while True:
#     led.on();  sleep(1)
#     led.off(); sleep(1)
