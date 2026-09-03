#define led 3
#define ldr A0

int ldrData;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  ldrData=analogRead(ldr);
  delay(50);
  if(ldrData > 90){
    digitalWrite(led, LOW);
  }
  else{
    digitalWrite(led, HIGH);
  }

}
