#include <Servo.h>

// ======== pinos ========
  // movimento para os lados
  int joystick_dir_x = A0 ;  
  Servo servo_esq_dir;

  // movimento para cima e para baixo
  int joystick_dir_y = A1 ;
  Servo servo_frente_tras;

  ////
  int joystick_dir_b =  3 ; 

  ////
  int joystick_esq_x = A2 ;
  
  // movimento para frente/tras
  int joystick_esq_y = A3 ;
  Servo servo_cima_baixo;

  // movimento para abrir e fechar a garra 
  int joystick_esq_b =  4 ;
  Servo servo_abrir_fechar;

//


// ======== configurações do joystick ========
  // limita os valores do joystick para não se mover sosinho 
  int limite_max = 700 ;
  int limite_min = 312 ;


//
  

// ======== movimentação ========
  // angulo que o servo faz quando algo está ativo
  int angulo_mov = 5 ;
  
  // indica a posição horizontal, para o lado esquerdo ou direito, o angulo de inicial é 55
  int posicao_esq_dir = 55; 
  
  // indica a posição vertical, para cima ou para baixo, o angulo de inicial é 100
  int posicao_frente_tras = 100; 
 
  // indica a posição para cima ou para baixo, o angulo inicial é 80
  int posicao_cima_baixo = 80;

  // indica se a garra está aberta ou fechada, o angulo inicial é 0
  int posicao_abrir_fechar = 0; 

//


void setup()
{
 // joystick
  pinMode(joystick_dir_x, INPUT);
  pinMode(joystick_dir_y, INPUT);
  pinMode(joystick_dir_b, INPUT_PULLUP);
  pinMode(joystick_esq_x, INPUT);
  pinMode(joystick_esq_y, INPUT);
  pinMode(joystick_esq_b, INPUT_PULLUP);
 //

 // servos 
  servo_esq_dir.attach(9);
  servo_cima_baixo.attach(10);
  servo_frente_tras.attach(11);
  servo_abrir_fechar.attach(12);
 //

 // serial
  Serial.begin(9600);
 //

}

// retorna +1, -1 ou 0 conforme a direção do joystick
int direcao(int valor)
{
  if (valor > limite_max)  return  1;
  if (valor < limite_min) return -1;
  return 0;
}

void loop()
{

  // ============ result joystick ============

    int j_dir_x = analogRead(joystick_dir_x); // esq_dir
    int j_dir_y = analogRead(joystick_dir_y); // cim_baix
    bool j_dir_b = digitalRead(joystick_dir_b); // reset

    int j_esq_x = analogRead(joystick_esq_x); // garra
    int j_esq_y = analogRead(joystick_esq_y); //frente_tras
    bool j_esq_b = digitalRead(joystick_esq_b); // reset

  //

  // ============ prints no serial ============
    // Serial.print(" | j_dir_x: ");  Serial.print(j_dir_x);
    // Serial.print(" | j_dir_y: "); Serial.print(j_dir_y);
    // Serial.print(" | j_dir_b: "); Serial.print(j_dir_b);
    // Serial.print(" | j_esq_x: "); Serial.print(j_esq_x);
    // Serial.print(" | j_esq_y: "); Serial.print(j_esq_y);
    // Serial.print(" | j_esq_b: "); Serial.println(j_esq_b);
    // Serial.println(" ========= ");
    // Serial.print(" | esq/dir: ");     Serial.print(posicao_esq_dir);
    // Serial.print(" | cima/baixo: "); Serial.print(posicao_cima_baixo);
    // Serial.print(" | frente/tras: "); Serial.print(posicao_frente_tras);
    // Serial.print(" | garra: ");      Serial.println(posicao_abrir_fechar);
    // Serial.println(" ========= ");

  //

  // ============ esquerda direita ============
    posicao_esq_dir += direcao(j_dir_x) * angulo_mov;
    posicao_esq_dir = constrain(posicao_esq_dir, 0, 180); // restringe a posição para não passar dos valores do servo 
  //

  // ============ cima baixo ============
    posicao_cima_baixo += direcao(j_dir_y) * angulo_mov;
    posicao_cima_baixo = constrain(posicao_cima_baixo, 0, 180);
  //

  // ============ frente tras ============
    posicao_frente_tras += direcao(j_esq_y) * angulo_mov;
    posicao_frente_tras = constrain(posicao_frente_tras, 0, 180);
  //

  // ============ abrir e fechar ============
    posicao_abrir_fechar += direcao(j_esq_x) * angulo_mov;
    posicao_abrir_fechar = constrain(posicao_abrir_fechar, 0, 180);

  //

  // ============ reset ============
    if (j_dir_b == HIGH && j_esq_b == HIGH ) {
      posicao_esq_dir = 55;
      posicao_cima_baixo = 80;
      posicao_frente_tras = 100;
      posicao_abrir_fechar = 180;
    }
  //

  // ============ servos motores ============
    servo_esq_dir.write(posicao_esq_dir);
    servo_cima_baixo.write(posicao_cima_baixo);
    servo_frente_tras.write(posicao_frente_tras);
    servo_abrir_fechar.write(posicao_abrir_fechar);
  //

  delay(68);

}






