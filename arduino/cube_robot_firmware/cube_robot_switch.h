#ifndef INCLUDE_CUBE_ROBOT_SWITCH_H_
#define INCLUDE_CUBE_ROBOT_SWITCH_H_

#include "cube_robot_operations.h"

#define RR 65
#define RI 66
#define R2 67
#define LL 68
#define LI 69
#define L2 70
#define UU 71
#define UI 72
#define U2 73
#define DD 74
#define DI 75
#define D2 76
#define FF 77
#define FI 78
#define F2 79
#define BB 80
#define BI 81
#define B2 82

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
