// C++ code
//

int led_verm = 2;
int led_am = 3;
int led_verd = 4;

void setup()
{
  pinMode(led_verm, OUTPUT);
  pinMode(led_am, OUTPUT);
  pinMode(led_verd, OUTPUT);
}

void loop()
{
  
  digitalWrite(led_verd, HIGH);
  delay(1000); // Wait for 10 millisecond(s)
  digitalWrite(led_verd, LOW);
  delay(1000);
  
  
  digitalWrite(led_am, HIGH);
  delay(1000); // Wait for 10 millisecond(s)
  digitalWrite(led_am, LOW);
  
  digitalWrite(led_verm, HIGH);
  delay(1000); // Wait for 10 millisecond(s)
  digitalWrite(led_verm, LOW);
}
