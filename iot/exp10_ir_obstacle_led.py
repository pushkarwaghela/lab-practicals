"""
Experiment 10: Raspberry Pi with IR sensor - detect obstacle and notify the user using LED
Wiring:  IR module VCC -> 3.3V (pin 1)   GND -> GND (pin 6)   OUT -> GPIO17 (pin 11)
         LED: GPIO27 (pin 13) -> 330 ohm resistor -> LED anode ; LED cathode -> GND
Most IR obstacle modules (FC-51) give OUT = LOW when an obstacle is detected and HIGH otherwise.
If your module works the other way round, set OBSTACLE_LEVEL = 1.
Run:     python3 exp10_ir_obstacle_led.py          (Ctrl+C to stop)
"""
import time
import RPi.GPIO as GPIO

IR_PIN = 17
LED_PIN = 27
OBSTACLE_LEVEL = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

try:
    print("IR obstacle detection started (Ctrl+C to stop)")
    while True:
        if GPIO.input(IR_PIN) == OBSTACLE_LEVEL:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Obstacle detected! LED ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No obstacle. LED OFF")
        time.sleep(0.3)
except KeyboardInterrupt:
    print("\nStopped by user")
finally:
    GPIO.cleanup()
