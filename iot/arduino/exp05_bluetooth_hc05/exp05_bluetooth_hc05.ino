/*
  Experiment 5: Wireless communication between Arduino and PC using Bluetooth (HC-05)
  Wiring (SoftwareSerial, so USB upload and Serial Monitor keep working):
     HC-05 VCC -> 5V        HC-05 GND -> GND
     HC-05 TXD -> D10 (Arduino RX)
     HC-05 RXD -> D11 (Arduino TX) through a voltage divider (1K in series + 2K to GND) because HC-05 RX is 3.3 V
     LED on D13
  If you wire HC-05 to D0/D1 as in the manual figure, use 'Serial' instead of 'BT' and unplug
  the HC-05 TX/RX wires while uploading.

  On the PC: pair with "HC-05" (password 1234 or 0000), note the COM port Windows creates,
  open it in a terminal (PuTTY / Serial Monitor of another IDE / Tera Term) at 9600 baud.
     send '1' -> LED ON      send '0' -> LED OFF     anything you type is shown in Arduino's Serial Monitor
*/
#include <SoftwareSerial.h>

SoftwareSerial BT(10, 11);     // RX, TX
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);          // USB Serial Monitor
  BT.begin(9600);              // HC-05 default baud rate
  Serial.println("Bluetooth ready. Send 1 to turn LED ON, 0 to turn it OFF.");
  BT.println("Arduino connected. Send 1 (ON) or 0 (OFF).");
}

void loop() {
  if (BT.available()) {                       // PC -> Arduino
    char c = BT.read();
    Serial.print("Received from PC: ");
    Serial.println(c);
    if (c == '1') {
      digitalWrite(ledPin, HIGH);
      BT.println("LED is ON");
    } else if (c == '0') {
      digitalWrite(ledPin, LOW);
      BT.println("LED is OFF");
    }
  }
  if (Serial.available()) {                   // Arduino Serial Monitor -> PC
    BT.write(Serial.read());
  }
}
