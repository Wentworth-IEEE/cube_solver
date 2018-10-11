#ifndef INCLUDE_CUBE_ROBOT_OPERATIONS_H_
#define INCLUDE_CUBE_ROBOT_OPERATIONS_H_


//define all motor pins
#define RIGHT_MOTOR_PIN 0
#define RIGHT_MOTOR_DIR_PIN 0
#define LEFT_MOTOR_PIN 0
#define LEFT_MOTOR_DIR_PIN 0
#define UP_MOTOR_PIN 0
#define UP_MOTOR_DIR_PIN 0
#define DOWN_MOTOR_PIN 0
#define DOWN_MOTOR_DIR_PIN 0
#define FRONT_MOTOR_PIN 0
#define FRONT_MOTOR_DIR_PIN 0
#define BACK_MOTOR_PIN 0
#define BACK_MOTOR_DIR_PIN 0

//define step sizes
#define QUARTER_TURN 0
#define HALF_TURN 0

//define direction
#define CLOCKWISE 0
#define COUNTER_CLOCKWISE 0

void Right(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = RIGHT_MOTOR_PIN;
    *dir_pin = RIGHT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void RightInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = RIGHT_MOTOR_PIN;
    *dir_pin = RIGHT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void DoubleRight(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = RIGHT_MOTOR_PIN;
    *dir_pin = RIGHT_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = CLOCKWISE;
}

void Left(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = LEFT_MOTOR_PIN;
    *dir_pin = LEFT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void DoubleLeft(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = LEFT_MOTOR_PIN;
    *dir_pin = LEFT_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void LeftInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = LEFT_MOTOR_PIN;
    *dir_pin = LEFT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void Up(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = UP_MOTOR_PIN;
    *dir_pin = UP_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void DoubleUp(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = UP_MOTOR_PIN;
    *dir_pin = UP_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = CLOCKWISE;
}

void UpInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = UP_MOTOR_PIN;
    *dir_pin = UP_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void Down(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = DOWN_MOTOR_PIN;
    *dir_pin = DOWN_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void DoubleDown(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = DOWN_MOTOR_PIN;
    *dir_pin = DOWN_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = CLOCKWISE;
}

void DownInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = DOWN_MOTOR_PIN;
    *dir_pin = DOWN_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void Front(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = FRONT_MOTOR_PIN;
    *dir_pin = FRONT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void DoubleFront(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = FRONT_MOTOR_PIN;
    *dir_pin = FRONT_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = CLOCKWISE;
}

void FrontInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = FRONT_MOTOR_PIN;
    *dir_pin = FRONT_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

void Back(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = BACK_MOTOR_PIN;
    *dir_pin = BACK_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = CLOCKWISE;
}

void DoubleBack(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = BACK_MOTOR_PIN;
    *dir_pin = BACK_MOTOR_DIR_PIN;
    *steps =  HALF_TURN;
    *dir = CLOCKWISE;
}

void BackInverse(int* motor_pin, int* dir_pin, int* steps, int* dir)
{
    *motor_pin = BACK_MOTOR_PIN;
    *dir_pin = BACK_MOTOR_DIR_PIN;
    *steps =  QUARTER_TURN;
    *dir = COUNTER_CLOCKWISE;
}

#endif  // INCLUDE_CUBE_ROBOT_OPERATIONS_H_
