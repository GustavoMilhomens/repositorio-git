#include <Servo.h>

int button = 2;
int led = 5;
Servo servo1;
Servo servo2;

void setup() 
{
  pinMode(button, INPUT);
  pinMode(led, OUTPUT);
  servo1.attach(8);
  servo2.attach(9);
  Serial.begin(9600);
}
void loop() 
{
  int result_btn = digitalRead(button);

  Serial.println(result_btn);

  while (result_btn == 1) {
    
    Serial.print("while");
    Serial.println(result_btn);

    digitalWrite(led, HIGH);
    
    servo1.write(90);
    servo2.write(90);
    // delay(100);
    // servo1.write(0);
    // servo2.write(0);
    // delay(100);

    result_btn = digitalRead(button);
  }


  // servo1.write(180);
  // servo2.write(45);
  // delay(10);
  // servo1.write(0);
  // servo2.write(0);
  // delay(10);
  
  digitalWrite(led, LOW);

  servo1.write(0);
  servo2.write(0);
  
  
  
}