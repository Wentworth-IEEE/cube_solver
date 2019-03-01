#define BAUD_RATE 9600

struct Motor 
{
    int step_pin;
    int dir_pin;
};

static constexpr Motor nullmotor = {0,0};

struct Instruction
{
    const Motor * motor;
    unsigned int steps;
    unsigned int dir;
    unsigned int safe_op2;
};

struct Task
{
    bool operator()()
    {
        auto cur_time = micros();
        if (cur_time > next_step)
        {
            next_step = cur_time + 100;
            digitalWrite(ins.motor->step_pin, HIGH);
            pin_state = HIGH;
            if (!(ins.steps--)) return done();
        }
        else
        {
            digitalWrite(ins.motor->step_pin, LOW);
            pin_state = LOW;
        }
    }
    void operator()(const Instruction & inst)
    {
        ins.motor = inst.motor;
        ins.steps = inst.steps;
        ins.dir = inst.dir;
        pin_state = LOW;
        next_step = 0;
        digitalWrite(ins.motor->dir_pin, ins.dir);
        this->operator()();
    }
 private:
     Instruction ins;
     unsigned long next_step;
     unsigned int steps_left;
     bool pin_state;

     bool done()
     {
        delayMicroseconds(20);
        digitalWrite(ins.motor->step_pin, LOW);
        ins.motor = &nullmotor;
        ins.steps = 0;
        ins.dir = 0;
        next_step = ~((unsigned long) 0);
     }
};

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

constexpr unsigned int Steps[] = 
{
    400u,  // Quarter turn
    800u   // Half turn
};

void OpCodeTranslation(unsigned char code, Instruction & ins)
{
    code -= 65;  // ASCII offset
    unsigned char motor_index = code / 3;
    unsigned char per_motor_code = code % 3;
    ins.motor = &Motors[motor_index];
    ins.steps = Steps[per_motor_code >> 1];
    ins.dir = per_motor_code == 1;
    ins.safe_op2 = motor_index ^ 1;
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

static Task primary;

//loop through all opcodes
void loop() {
  // put your main code here, to run repeatedly:
  if (!primary())
  {
    OpCodeTranslation(Serial.read(), next_instruction);
    primary(next_instruction);
  }

//   digitalWrite(next_instruction.motor->dir_pin, next_instruction.dir);
//   for (; next_instruction.steps > 0; --next_instruction.steps)
//   {
//     delayMicroseconds(100);
//     digitalWrite(next_instruction.motor->step_pin, HIGH);
//     delayMicroseconds(25);
//     digitalWrite(next_instruction.motor->dir_pin, LOW);
//   }

}
