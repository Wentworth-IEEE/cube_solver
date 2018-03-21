#include "cube_robot_switch.h"

#define MAX_ACTIVE_FUNCTIONS 2
#define BAUD_RATE 9600

//define other global variables
unsigned char active_functions;

int motor_pin, dir_pin, steps, dir;

//setup anything that needs setting up
void setup() {
  // put your setup code here, to run once:
 Serial.begin(BAUD_RATE);
 Serial.flush();
 active_functions = 0;
}

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:
  OpCodeSwitch(Serial.read(), &motor_pin, &dir_pin, &steps, &dir);
  digitalWrite(dir_pin, dir);
  for (int i = 0; i < steps; i++){
    digitalWrite(motor_pin, HIGH);
    digitalWrite(motor_pin, LOW);
  }
}
