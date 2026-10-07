
#include <Servo.h>

// ======== pinos ========
  int button_direita = 2;
  int button_esquerda = 3;
  Servo servo_esq_dir;

  int button_cima = 4;
  int button_baixo = 5;
  Servo servo_cima_baixo;

  int button_frente = 6;
  int button_tras = 7;
  Servo servo_frente_tras;

  int button_abrir_fechar = 8;
  Servo servo_abrir_fechar;


// ======== variaveis de movimentação ========
  int angulo_mov = 5 ; // determina qqual o angulo que será passado por click

  // rotação para os lados, eixo x
    int result_btn_esq = 0; // rotação para a esquerda 
    int result_btn_dir = 0; // rotação para a direita

    int position_esq_dir = 55; // indica a posição horizontal, para o lado esquerdo ou direito, o angulo de centralizção é 55

  // movimentação cima baixo, eixo y
    int result_btn_cima = 0;
    int result_btn_baixo = 0;

    int position_cima_baixo = 80;

  // movimentação frente tras, eixo z
    int result_btn_frente = 0;
    int result_btn_tras = 0;

    int position_frente_tras = 100;

  // garra abrir_fechar 

    bool result_btn_abrir_fechar;

    int position_abrir_fechar = 0;

void setup() 
{

// butões
  pinMode(button_esquerda, INPUT);
  pinMode(button_direita, INPUT);

  pinMode(button_cima, INPUT);
  pinMode(button_baixo, INPUT);

  pinMode(button_frente, INPUT);
  pinMode(button_tras, INPUT);

  pinMode(button_abrir_fechar, INPUT);

// servos motores
  servo_esq_dir.attach(9);
  servo_cima_baixo.attach(10);
  servo_frente_tras.attach(11);
  servo_abrir_fechar.attach(12);

// serial
  Serial.begin(9600);
}

void loop() 
{
// result button
  result_btn_esq = digitalRead(button_esquerda);
  result_btn_dir = digitalRead(button_direita);
  //delay(100);
  result_btn_cima = digitalRead(button_cima);
  result_btn_baixo = digitalRead(button_baixo);

  result_btn_frente = digitalRead(button_frente);
  result_btn_tras = digitalRead(button_tras);


  if ( digitalRead(button_abrir_fechar) == 1){
    if (result_btn_abrir_fechar == 1){
      result_btn_abrir_fechar = 0 ;
    }
    else if (result_btn_abrir_fechar == 0){
      result_btn_abrir_fechar = 1 ;
    }
  }
  

// =============== prints no sereal ===============
  // Serial.print("esquerda: ");
  // Serial.println(result_btn_esq);
  
  // Serial.print("direita: ");
  // Serial.println(result_btn_dir);
  
  Serial.print("cima: ");
  Serial.println(result_btn_cima);
  
  // Serial.print("garra: ");
  // Serial.println(result_btn_abrir_fechar);
  
  Serial.print("positoin: ");
  Serial.println(position_cima_baixo);
  delay(100); // delay para melhor visualização das saidas e para melhor funcionalidade do codigo

// =============== esquerda direita ===============

  if (result_btn_dir == 1 && result_btn_esq == 1) {// reseta para a posição que deve ser a inicial
    position_esq_dir = 55 ;
  }

  else if (result_btn_esq == 1 && position_esq_dir <= 180 ){
    position_esq_dir += angulo_mov ; 
  }

  else if (result_btn_dir == 1 && position_esq_dir >= 0 ){
    position_esq_dir -= angulo_mov ; 
  }

  else{
    ;
  }

// =============== cima baixo ===============

  if (result_btn_cima == 1 && position_cima_baixo <= 180 ){
    position_cima_baixo += angulo_mov ; 
  }

  else if (result_btn_baixo == 1 && position_cima_baixo >= 50 ){
    position_cima_baixo -= angulo_mov ; 
  }

  else{
    ;
  }

// =============== frente tras ===============

  if (result_btn_frente == 1 && position_frente_tras <= 180 ){
    position_frente_tras += angulo_mov ; 
  }

  else if (result_btn_tras == 1 && position_frente_tras >= 0 ){
    position_frente_tras -= angulo_mov ; 
  }

  else{
    ;
  }

// =============== abrir e fechar ===============

  if (result_btn_abrir_fechar == 1){
    position_abrir_fechar = 180 ; 
  }

  else if (result_btn_abrir_fechar == 0){
    position_abrir_fechar = 0 ; 
  }

  else{
    ;
  }

// =============== servos motores =============== 

  servo_esq_dir.write(position_esq_dir);
  servo_cima_baixo.write(position_cima_baixo);
  servo_frente_tras.write(position_frente_tras);
  servo_abrir_fechar.write(position_abrir_fechar);
}

 
  