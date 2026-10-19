/*
  Experiment 2 (a): Interfacing LDR with Arduino
  Wiring (voltage divider): 5V -> LDR -> A0 ; A0 -> 100K resistor -> GND
  Open Serial Monitor at 9600 baud. Bright light gives high values (about 800-1023),
  covering the LDR gives low values.
*/
int sensorPin = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(sensorPin);   // 0 - 1023
  Serial.print("LDR value: ");
  Serial.println(sensorValue);
  delay(500);
}
