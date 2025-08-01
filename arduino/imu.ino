#include <Wire.h>
#include <Adafruit_BNO055.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void setup() {
  Serial.begin(9600);
  if (!bno.begin()) {
    Serial.println("BNO055 not detected");
    while (1);
  }
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd == "GET_HEADING") {
      sensors_event_t orientationData;
      bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
      Serial.println(orientationData.orientation.x);  // heading 角度
    }
  }
}