// C++ code// C++
//
int led_verde = 2; // pino do led verde
int led_amarel = 3; // pino do led amarelo
int led_verm = 4; // pino do led vermelho
int buzer_pin = 5; // pino do buzzer
int echo_pin = 6; // pino do echo do sensor
int trig_pin = 7; // pino do trig do sensor


int limite_distanc = 50; // limite de distancia
int cm = 0; // centimetros

long ler_distancia_sensor(int t_pin, int e_pin)
{
    
    pinMode(t_pin, OUTPUT); // determina o pino do trig/disparo do sensor como saida/output 
    digitalWrite(t_pin, LOW); // deixa o pino em nivel baixo/desligado
    delayMicroseconds(2); // espera de 2 microsegundos

    digitalWrite(t_pin, HIGH); // faz o sensor emitir som colocando em nivel alto/ligado
    delayMicroseconds(10); 
    digitalWrite(t_pin, LOW);
    pinMode(e_pin, INPUT); // configura o pino echo como entrada entrada/input

    return pulseIn(e_pin, HIGH); // retorna ficar em hing e retorna o tempo levado em micrisegundos 

}

void setup()
{
    Serial.begin(9600); // inicia a cominicação em 9600 bits/segundo
    pinMode(led_verde, OUTPUT); // configura o pino verde como saida 
    pinMode(led_amarel, OUTPUT); // configura o pino amarelo como saida
    pinMode(led_verm, OUTPUT); // configura o pino vermelho como saida
    pinMode(buzer_pin, OUTPUT); // configura o buzzer como saida  
}

void loop()
{
    cm = 0.01723 * ler_distancia_sensor( trig_pin , echo_pin); // converte o valor em centimetros com base nos microsegundos 
    Serial.print("cm: ");
    Serial.print(cm);
    Serial.print("");



    if (cm > limite_distanc) // se a distancia em cm for maior que o limite não manda nenhum sinal aos leds 
    {
        digitalWrite(led_verde, LOW);
        digitalWrite(led_amarel, LOW);
        digitalWrite(led_verm, LOW);      

    }

    if (cm <= limite_distanc && cm > limite_distanc * 0.5) // se a distancia em cm for menor que o limite e maior que o limite - 100 não manda sinal ao led verde
    {
        digitalWrite(led_verde, HIGH);
        digitalWrite(led_amarel, LOW);
        digitalWrite(led_verm, LOW);

        digitalWrite(buzer_pin, HIGH);
        delay(100);
      	digitalWrite(buzer_pin, LOW);
        delay(800);
    }

    if (cm <= limite_distanc * 0.5 && cm > limite_distanc * 0.2 ) // se a distancia em cm for menor que o limite e maior que o limite - 100 não manda sinal ao led verde
    {
        digitalWrite(led_verde, LOW);
        digitalWrite(led_amarel, HIGH);
        digitalWrite(led_verm, LOW);

        digitalWrite(buzer_pin, HIGH);
        delay(100);
      	digitalWrite(buzer_pin, LOW);
      	delay(400);


    }

    if (cm <= limite_distanc * 0.2 && cm >= 0 ) // se a distancia em cm for menor que o limite e maior que o limite - 100 não manda sinal ao led verde
    {
        digitalWrite(led_verde, LOW);
        digitalWrite(led_amarel, LOW);
        digitalWrite(led_verm, HIGH );

        digitalWrite(buzer_pin, HIGH);
        delay(100);
      	digitalWrite(buzer_pin, LOW);
        delay(50);

    }
}