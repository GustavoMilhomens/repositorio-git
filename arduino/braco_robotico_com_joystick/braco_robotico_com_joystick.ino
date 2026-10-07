#include <Servo.h>

// ======== pinos ========

  int joystick_dir_x = A0 ;
  int joystick_dir_y = A1 ;
  int joystick_dir_b =  3 ;

  int joystick_esq_x = A2 ;
  int joystick_esq_y = A3 ;
  int joystick_esq_b =  4 ;

  Servo servo_esq_dir;
  Servo servo_cima_baixo;
  Servo servo_frente_tras;
  Servo servo_abrir_fechar;

// ======== ajustes do joystick ========
  int limiar_alto = 700;
  int limiar_baixo = 324;

  // se algum eixo estiver invertido, troque entre 1 e -1
  int inverte_esq_dir = 1;
  int inverte_cima_baixo = 1;
  int inverte_frente_tras = 1;

// ======== variaveis de movimentação ========
  int angulo_mov = 5; // ângulo somado/subtraído a cada ciclo

  int position_esq_dir = 55;
  int position_cima_baixo = 80;
  int position_frente_tras = 100;

  bool result_btn_abrir_fechar = false;
  int position_abrir_fechar = 0;

  bool anterior_dir_b = HIGH;
  bool anterior_esq_b = HIGH;

void setup()
{
  pinMode(joystick_dir_x, INPUT);
  pinMode(joystick_dir_y, INPUT);
  pinMode(joystick_dir_b, INPUT_PULLUP);
  pinMode(joystick_esq_x, INPUT);
  pinMode(joystick_esq_y, INPUT);
  pinMode(joystick_esq_b, INPUT_PULLUP);

  servo_esq_dir.attach(9);
  servo_cima_baixo.attach(10);
  servo_frente_tras.attach(11);
  servo_abrir_fechar.attach(12);

  servo_esq_dir.write(position_esq_dir);
  servo_cima_baixo.write(position_cima_baixo);
  servo_frente_tras.write(position_frente_tras);
  servo_abrir_fechar.write(position_abrir_fechar);

  Serial.begin(9600);
}

// retorna +1, -1 ou 0 conforme a direção do joystick
int direcao(int valor, int inverte)
{
  if (valor > limiar_alto)  return  1 * inverte;
  if (valor < limiar_baixo) return -1 * inverte;
  return 0;
}

void loop()
{
// ============ leituras ============
  int dir_x = analogRead(joystick_dir_x);
  int dir_y = analogRead(joystick_dir_y);
  bool dir_b = digitalRead(joystick_dir_b);

  int esq_x = analogRead(joystick_esq_x); // não usado
  int esq_y = analogRead(joystick_esq_y);
  bool esq_b = digitalRead(joystick_esq_b);

// ============ prints no serial ============
  Serial.print("dir_x: ");  Serial.print(dir_x);
  Serial.print(" | dir_y: "); Serial.print(dir_y);
  Serial.print(" | dir_b: "); Serial.print(dir_b);
  Serial.print(" | esq_x: "); Serial.print(esq_x);
  Serial.print(" | esq_y: "); Serial.print(esq_y);
  Serial.print(" | esq_b: "); Serial.println(esq_b);

  Serial.print("esq/dir: ");     Serial.print(position_esq_dir);
  Serial.print(" | cima/baixo: "); Serial.print(position_cima_baixo);
  Serial.print(" | frente/tras: "); Serial.print(position_frente_tras);
  Serial.print(" | garra: ");      Serial.println(position_abrir_fechar);

// ============ esquerda direita (joystick dir, eixo X) ============
  position_esq_dir += direcao(dir_x, inverte_esq_dir) * angulo_mov;
  position_esq_dir = constrain(position_esq_dir, 0, 180);

// ============ cima baixo (joystick dir, eixo Y) ============
  position_cima_baixo += direcao(dir_y, inverte_cima_baixo) * angulo_mov;
  position_cima_baixo = constrain(position_cima_baixo, 50, 180);

// ============ frente tras (joystick esq, eixo Y) ============
  position_frente_tras += direcao(esq_y, inverte_frente_tras) * angulo_mov;
  position_frente_tras = constrain(position_frente_tras, 0, 180);

// ============ abrir e fechar (botão joystick dir) ============
  if (dir_b == LOW && anterior_dir_b == HIGH) {
    result_btn_abrir_fechar = !result_btn_abrir_fechar;
  }
  anterior_dir_b = dir_b;

  if (result_btn_abrir_fechar) {
    position_abrir_fechar = 180;
  }
  else {
    position_abrir_fechar = 0;
  }

// ============ reset posição inicial (botão joystick esq) ============
  if (esq_b == LOW && anterior_esq_b == HIGH) {
    position_esq_dir = 55;
    position_cima_baixo = 80;
    position_frente_tras = 100;
  }
  anterior_esq_b = esq_b;

// ============ servos motores ============
  servo_esq_dir.write(position_esq_dir);
  servo_cima_baixo.write(position_cima_baixo);
  servo_frente_tras.write(position_frente_tras);
  servo_abrir_fechar.write(position_abrir_fechar);

  delay(100);
}