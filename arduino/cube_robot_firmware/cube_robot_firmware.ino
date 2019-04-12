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
    {2, 22},  // Right
    {3, 24},  // Left
    {10, 26},  // Up
    {5, 28},  // Down
    {6, 30},  // Front
    {4, 32}   // Back
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
 for (int i = 0; i < 6; i++)
 {
     pinMode(Motors[i].step_pin, OUTPUT);
     pinMode(Motors[i].dir_pin, OUTPUT);
     digitalWrite(Motors[i].step_pin, LOW);
     digitalWrite(Motors[i].dir_pin, LOW);
 }
}

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    OpCodeTranslation(Serial.read(), next_instruction);
    digitalWrite(next_instruction.motor->dir_pin, next_instruction.dir);
    for (; next_instruction.steps > 0; --next_instruction.steps)
    {
        delayMicroseconds(400);
        digitalWrite(next_instruction.motor->step_pin, HIGH);
        delayMicroseconds(200);
        digitalWrite(next_instruction.motor->step_pin, LOW);
    }
  }
}
