/*
  Experiment 3 (b): Interfacing DHT11 temperature and humidity sensor with Arduino
  Libraries (Sketch > Include Library > Manage Libraries):
     "DHT sensor library" by Adafruit  and  "Adafruit Unified Sensor"
  Wiring: VCC -> 5V, DATA -> D2 (with 10K pull-up to 5V if you use the bare 4-pin sensor), GND -> GND
  DHT11 can give a new reading only once every 2 seconds.
*/
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();       // Celsius

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %   Temperature: ");
  Serial.print(t);
  Serial.println(" C");
}
