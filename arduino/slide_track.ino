#include <Stepper.h>  // Include the Stepper motor library

const int stepsPerRevolution = 2048;  // Number of steps per full revolution (for 28BYJ-48 motor)

Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);  // Initialize the stepper motor with 4 control pins

void setup() {
  myStepper.setSpeed(15);  // Set motor speed to 15 RPM (rotations per minute)
}

void loop() {
  myStepper.step(5000);    // Move the motor forward 9000 steps
  delay(500);              // Wait for 0.5 seconds
  myStepper.step(-5000);   // Move the motor backward 9000 steps
  delay(500);              // Wait for 0.5 seconds
}
