#include "cube_robot_operations.h"
#define MAX_ACTIVE_FUNCTIONS 2

//define other global variables
unsigned char active_functions;

int motor_pin, dir_pin, steps, dir;

//setup anything that needs setting up
void setup() {
  // put your setup code here, to run once:
 Serial.Begin();
 Serial.Flush();
 active_functions = 0;
}

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:
  OpCodeSwitch(Serial.Read(), &motor_pin, &dir_pin, &steps, &dir);
  digitalWrite(dir_pin, dir);
  for (int i = 0; i < steps; i++){
    digitalWrite(motor_pin, 1);
    digitalWrite(motor_pin, 0);
  }
}
