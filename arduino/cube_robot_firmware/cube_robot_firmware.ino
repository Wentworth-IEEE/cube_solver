#define BAUD_RATE 9600

typedef struct Motor 
{
    int step_pin;
    int dir_pin;
} Motor;

typedef struct Instruction
{
    const Motor * motor;
    unsigned int steps;
    unsigned int dir;
} Instruction;

static struct IBuff
{
    Instruction buffer[8];
    unsigned char head;
    unsigned char tail;
    const unsigned char size = 8;
} IBuff;

static const Motor Motors[] = 
{
    {10, 0},  // Right
    {11, 0},  // Left
    {12, 0},  // Up
    {13, 0},  // Down
    {14, 0},  // Front
    {15, 0}   // Back
};

static const unsigned int Steps[] = 
{
    400u,  // Quarter turn
    800u   // Half turn
};

void OpCodeTranslation(unsigned char code, Instruction & ins)
{
    code -= 65;  // ASCII offset
    unsigned char per_motor_code = code % 3;
    ins.motor = &Motors[code / 3];
    ins.steps = Steps[per_motor_code >> 1];
    ins.dir = per_motor_code == 1;
}

//define other global variables
unsigned char active_functions;
Instruction next_instruction;

//setup anything that needs setting up
void setup() {
  // put your setup code here, to run once:
 Serial.begin(BAUD_RATE);
 Serial.flush();
 active_functions = 0;
 for (int i = 0; i < 5; i++)
 {
     pinMode(Motors[i].step_pin, OUTPUT);
     pinMode(Motors[i].dir_pin, OUTPUT);
 }
}

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:
  OpCodeTranslation(Serial.read(), next_instruction);
  digitalWrite(next_instruction.motor->dir_pin, next_instruction.dir);
  for (; next_instruction.steps > 0; --next_instruction.steps)
  {
    delayMicroseconds(100);
    digitalWrite(next_instruction.motor->step_pin, HIGH);
    delayMicroseconds(25);
    digitalWrite(next_instruction.motor->dir_pin, LOW);
  }
}
