//#include <DHT11.h>

#include <DHT.h>
#include <DHT_U.h>


#include "DHT.h"




#define DHTTYPE DHT11
const int DHTPIN = 2;// Pin donde está conectado el DHT11

DHT dht(DHTPIN, DHTTYPE);

#define LED_AZUL 6    // LED azul para indicar humedad
#define RELE 7        // Pin del relé que controla el LED amarillo
#define SENSOR_BATERIA A0


void setup() {
  Serial.begin(9600);
  Serial.println("Sensor de Temperatura y Humedad DHT11");
  pinMode(LED_AZUL, OUTPUT);
  pinMode(RELE, OUTPUT);
  dht.begin();
}

void loop() {

  delay(2000);
  // Leer humedad
  float humedad = dht.readHumidity();
  delay(10);
  //float temperatura = dht.readTemperature();
 // delay(10);


  //Serial.println(String(humedad));
  //Serial.print(String(temperatura));


  // Leer nivel de batería
  int lectura_bateria = analogRead(SENSOR_BATERIA);
  float voltaje_bateria = lectura_bateria * (9.0 / 1023.0);  // Conversión a voltaje real
  //Serial.print("Nivel de batería: ");
  //Serial.print(voltaje_bateria);
  //Serial.println(" V");
  
  Serial.print(String(humedad));
  Serial.print(",");
  Serial.println(String(voltaje_bateria));

  // Comportamiento del LED azul y el relé (LED amarillo) según la humedad
  if (humedad > 85) {
    // Si la humedad es mayor al 85%
    digitalWrite(RELE, HIGH);  // Encender el LED amarillo
    delay(250);                // LED amarillo parpadea cada 250 ms (más rápido)
    digitalWrite(RELE, LOW);
    delay(250);                // Mantener apagado por 250 ms
  } else if (humedad >80 && humedad <= 85) {
    // Si la humedad está entre 80% y 85%
    digitalWrite(LED_AZUL, HIGH);  // Mantener el LED azul encendido
    digitalWrite(RELE, HIGH);      // Mantener el relé (LED amarillo) encendido
  } else if (humedad > 55 && humedad <= 80) {
    // Si la humedad está entre 55% y 80%
    digitalWrite(LED_AZUL, HIGH);  // Encender el LED azul
    digitalWrite(RELE, HIGH);      // Encender el relé (LED amarillo)
    delay(5000);                   // Mantenerlos encendidos 5 segundos
    digitalWrite(LED_AZUL, LOW);   // Apagar el LED azul después de 5 segundos
  } else if (humedad <=25) {
    // Si la humedad es menor al 25%, el LED azul parpadea 3 veces
    for (int i = 0; i < 3; i++) {
      digitalWrite(LED_AZUL, HIGH);
      delay(500);  // Mantener encendido 500 ms
      digitalWrite(LED_AZUL, LOW);
      delay(500);  // Apagar 500 ms
    }
    delay(4000);  // Esperar 4 segundos antes de repetir
  } else {
    // Si la humedad está entre 25% y 55%, ambos LEDs se apagan
    digitalWrite(LED_AZUL, LOW);   // Apagar el LED azul
    digitalWrite(RELE, LOW);       // Apagar el relé (LED amarillo)
  }

  delay(2000);  // Pequeña pausa entre lecturas
}
