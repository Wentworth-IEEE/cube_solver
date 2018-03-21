#ifndef INCLUDE_CUBE_ROBOT_SWITCH_H_
#define INCLUDE_CUBE_ROBOT_SWITCH_H_

#include "cube_robot_operations.h"

#define RR 0
#define RI 1
#define R2 2
#define LL 3
#define LI 4
#define L2 5
#define UU 6
#define UI 7
#define U2 8
#define DD 9
#define DI 10
#define D2 11
#define FF 12
#define FI 13
#define F2 14
#define BB 15
#define BI 16
#define B2 17

void OpCodeSwitch(unsigned char code, int* motor_pin, int* dir_pin, int* steps, int* dir)
{
switch (code) {
  case RR:
    Right(motor_pin,  dir_pin,  steps,  dir);
    break;
  case RI:
    RightInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case R2:
    DoubleRight( motor_pin,  dir_pin,  steps,  dir);
    break;
  case LL:
    Left( motor_pin,  dir_pin,  steps,  dir);
    break;
  case LI:
    LeftInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case L2:
    DoubleLeft( motor_pin,  dir_pin,  steps,  dir);
    break;
  case UU:
    Up( motor_pin,  dir_pin,  steps,  dir);
    break;
  case UI:
    UpInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case U2:
    DoubleUp( motor_pin,  dir_pin,  steps,  dir);
    break;
  case DD:
    Down( motor_pin,  dir_pin,  steps,  dir);
    break;
  case DI:
    DownInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case D2:
    DoubleDown( motor_pin,  dir_pin,  steps,  dir);
    break;
  case FF:
    Front( motor_pin,  dir_pin,  steps,  dir);
    break;
  case FI:
    FrontInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case F2:
    DoubleFront( motor_pin,  dir_pin,  steps,  dir);
    break;
  case BB:
    Back( motor_pin,  dir_pin,  steps,  dir);
    break;
  case BI:
    BackInverse( motor_pin,  dir_pin,  steps,  dir);
    break;
  case B2:
    DoubleBack( motor_pin,  dir_pin,  steps,  dir);
    break;

}
}

#endif  // INCLUDE_CUBE_ROBOT_SWITCH_H_
