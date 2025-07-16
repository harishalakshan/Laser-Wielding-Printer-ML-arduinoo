
#include <Servo.h>
Servo laser;
int laserPin = 9;

void setup() {
  Serial.begin(9600);
  laser.attach(laserPin);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil(',');
    if (cmd == "on") digitalWrite(laserPin, HIGH);
    else if (cmd == "off") digitalWrite(laserPin, LOW);
    // Extend logic for move_x, move_y etc.
  }
}
