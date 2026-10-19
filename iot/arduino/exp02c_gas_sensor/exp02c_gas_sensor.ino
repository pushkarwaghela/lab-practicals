/*
  Experiment 2 (c): Interfacing gas sensor (MQ-3 module) with Arduino
  Wiring: VCC -> 5V, GND -> GND, AO -> A0, DO -> D2 ; LED on D13
  The MQ sensor needs 1-2 minutes to warm up. AO gives the gas concentration (0-1023),
  DO goes HIGH/LOW when the concentration crosses the threshold set with the module's preset
  (on most modules DO is LOW when gas is detected - check yours and flip the test if needed).
*/
int gasAnalog = A0;
int gasDigital = 2;
int ledPin = 13;
int threshold = 400;       // adjust after observing readings in clean air

void setup() {
  pinMode(gasDigital, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int value = analogRead(gasAnalog);
  int digitalState = digitalRead(gasDigital);

  Serial.print("Gas analog value: ");
  Serial.print(value);
  Serial.print("   Digital output: ");
  Serial.println(digitalState);

  if (value > threshold) {
    digitalWrite(ledPin, HIGH);
    Serial.println("Gas detected!");
  } else {
    digitalWrite(ledPin, LOW);
  }
  delay(500);
}
