#include "cube_robot_operations.h"
#include "cube_robot_switch.h"

#define MAX_ACTIVE_FUNCTIONS 2

//define other global variables
int activeFunctions;

//setup anything that needs setting up
void setup() {
  // put your setup code here, to run once:
 Serial.Begin();
 Serial.Flush();
 activeFunctions = 0;
}

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:


}
