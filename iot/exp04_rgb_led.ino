/*
  Experiment 4: Interfacing RGB LED with Arduino - display all possible colours
  Wiring (common cathode): R -> 330 ohm -> D9, G -> 330 ohm -> D10, B -> 330 ohm -> D11, common leg -> GND
  (common anode: common leg -> 5V and set COMMON_ANODE to true)
  D9, D10, D11 are PWM pins, so analogWrite() gives intermediate shades.
*/
const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;
const bool COMMON_ANODE = false;

void setColor(int r, int g, int b) {          // values 0-255
  if (COMMON_ANODE) {
    r = 255 - r;  g = 255 - g;  b = 255 - b;
  }
  analogWrite(redPin, r);
  analogWrite(greenPin, g);
  analogWrite(bluePin, b);
}

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Basic colours (see RGB table in the manual)
  Serial.println("Red");      setColor(255, 0, 0);      delay(1000);
  Serial.println("Green");    setColor(0, 255, 0);      delay(1000);
  Serial.println("Blue");     setColor(0, 0, 255);      delay(1000);
  Serial.println("Yellow");   setColor(255, 255, 0);    delay(1000);
  Serial.println("Magenta");  setColor(255, 0, 255);    delay(1000);
  Serial.println("Cyan");     setColor(0, 255, 255);    delay(1000);
  Serial.println("White");    setColor(255, 255, 255);  delay(1000);
  Serial.println("OFF");      setColor(0, 0, 0);        delay(1000);

  // Intermediate shades using PWM: orange, purple, pink
  Serial.println("Orange");   setColor(255, 100, 0);    delay(1000);
  Serial.println("Purple");   setColor(128, 0, 128);    delay(1000);
  Serial.println("Pink");     setColor(255, 105, 180);  delay(1000);

  // Smooth colour fade through red -> green -> blue -> red
  for (int i = 0; i <= 255; i++) { setColor(255 - i, i, 0);   delay(5); }
  for (int i = 0; i <= 255; i++) { setColor(0, 255 - i, i);   delay(5); }
  for (int i = 0; i <= 255; i++) { setColor(i, 0, 255 - i);   delay(5); }
}
