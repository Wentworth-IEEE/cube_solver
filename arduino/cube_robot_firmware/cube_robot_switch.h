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

void OpCodeSwitch(unsigned char code)
{
switch (code)) {
  case RR:
    Right();
    break;
  case RI:
    RightInverse();
    break;
  case R2:
    DoubleRight();
    break;
  case LL:
    Left();
    break;
  case LI:
    LeftInverse();
    break;
  case L2:
    DoubleLeft();
    break;
  case UU:
    Up();
    break
    case UI:
    UpInverse();
    break;
    case U2:
    DoubleUp();
    break;
    case DD:
    Down();
    break;
    case DI:
    DownInverse();
    break;
    case D2:
    DoubleDown();
    break;
    case FF:
    Front();
    break;
    case FI:
    FrontInverse();
    break;
    case F2:
    DoubleFront();
    break;
    case BB:
    Back();
    break;
    case BI:
    BackInverse();
    break;
    case B2:
    DoubleBack();
    break;

}
}
