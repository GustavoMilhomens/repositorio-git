
#include <Servo.h>

// pinos 
int button_direita = 2;
int button_esquerda = 3;
Servo servo_esq_dir;

// variaveis de movimentação 
int result_btn_esq = 1;
int result_btn_dir = 1;

int position_esq_dir = 55; // indica a posição horizontal, para o lado esquerdo ou direito, o angulo de centralizção é 55



void setup() 
{
  pinMode(button_direita, INPUT);
  pinMode(button_esquerda, INPUT);
  servo_esq_dir.attach(9);
  Serial.begin(9600);
}

void loop() 
{
  result_btn_esq = digitalRead(button_esquerda);
  result_btn_dir = digitalRead(button_direita);
  delay(100);

  Serial.print("esquerda: ");
  Serial.println(result_btn_esq);
  Serial.print("direita: ");
  Serial.println(result_btn_dir);
  Serial.print("positoin: ");
  Serial.println(position_esq_dir);

  if (result_btn_dir == 1 && result_btn_esq == 1) // reseta para a posição que deve ser a inicial
  {
    position_esq_dir = 55 ;
  }

  else if (result_btn_dir == 1 && position_esq_dir <= 180 )
  {
    position_esq_dir += 3 ; 
  }

  else if (result_btn_esq == 1 && position_esq_dir >= 0 )
  {
    position_esq_dir -= 3 ; 
  }

  else{
    ;
  }

  servo_esq_dir.write(position_esq_dir);
}

 
  