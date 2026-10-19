/*
  Experiment 2 (b): Interfacing touch sensor with Arduino
  Wiring: Touch sensor SIG -> D8, VCC -> 5V, GND -> GND ; LED on D13 (on-board LED)
  Serial Monitor (9600): prints "Sensor detected" when touched, else "Sensor not detected".
*/
int touchPin = 8;
int ledPin = 13;

void setup() {
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(touchPin) == HIGH) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Sensor detected");
  } else {
    digitalWrite(ledPin, LOW);
    Serial.println("Sensor not detected");
  }
  delay(300);
}
