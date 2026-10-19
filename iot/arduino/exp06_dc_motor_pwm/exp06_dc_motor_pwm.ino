/*
  Experiment 6: Interfacing DC motor with Arduino - speed control using PWM
  Components: PN2222 transistor, 1N4001 diode, 270 ohm resistor, small 6V DC motor
  Wiring:  D3 -> 270 ohm -> transistor base ; transistor emitter -> GND ;
           motor between +5V and transistor collector ; 1N4001 diode across the motor
           (striped end/cathode towards +5V). Flat side of the transistor faces the Arduino.
  Never drive the motor directly from an Arduino pin.

  Open Serial Monitor (9600, "No line ending"), type a value 0-255 and press Send.
*/
int motorPin = 3;               // PWM pin

void setup() {
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Speed 0 to 255");
}

void loop() {
  if (Serial.available()) {
    int speed = Serial.parseInt();          // read the number typed in the Serial Monitor
    if (speed >= 0 && speed <= 255) {
      analogWrite(motorPin, speed);         // PWM duty cycle = speed/255
      Serial.print("Motor speed set to ");
      Serial.println(speed);
    }
  }
}
