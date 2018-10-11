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
    Right(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case RI:
    RightInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case R2:
    DoubleRight(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case LL:
    Left(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case LI:
    LeftInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case L2:
    DoubleLeft(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case UU:
    Up(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case UI:
    UpInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case U2:
    DoubleUp(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case DD:
    Down(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case DI:
    DownInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case D2:
    DoubleDown(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case FF:
    Front(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case FI:
    FrontInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case F2:
    DoubleFront(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case BB:
    Back(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case BI:
    BackInverse(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;
  case B2:
    DoubleBack(int* motor_pin, int* dir_pin, int* steps, int* dir);
    break;

}
}
