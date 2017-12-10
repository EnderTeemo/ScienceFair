#include "CurieIMU.h"

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
while (!Serial); 


Serial.println("Intializing IMU device...")
CurieIMU.begin();

CurieIMU.setAccelerometerRange(2);
}

void loop() {
  // put your main code here, to run repeatedly:

}
