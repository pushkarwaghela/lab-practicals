/*
  Experiment 1: Interfacing LED with Arduino - blinking LED
  Wiring: Arduino pin -> 330 ohm resistor -> LED anode (long leg); LED cathode (short leg) -> GND
  Step 1: use the on-board LED / pin 13 (File > Examples > Basics > Blink)
  Step 2: move the jumper to D7 and change 'led' to 7 (as in the manual)
*/
int led = 7;            // use 13 first, then 7

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(led, HIGH);   // LED ON
  delay(1000);               // 1 second
  digitalWrite(led, LOW);    // LED OFF
  delay(1000);
}
