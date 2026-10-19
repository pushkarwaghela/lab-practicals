/*
  Experiment 3 (a): Interfacing LM35 temperature sensor with Arduino
  Wiring (flat side facing you, pins down): left pin VCC -> 5V, middle pin OUT -> A0, right pin GND -> GND
  LM35 gives 10 mV per degree Celsius (250 mV = 25 C).
*/
int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int reading = analogRead(sensorPin);
  float voltage = reading * (5.0 / 1023.0);     // volts
  float tempC = voltage * 100.0;                // 10 mV per C
  float tempF = (tempC * 9.0 / 5.0) + 32.0;

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.print(" C   ");
  Serial.print(tempF);
  Serial.println(" F");
  delay(1000);
}
