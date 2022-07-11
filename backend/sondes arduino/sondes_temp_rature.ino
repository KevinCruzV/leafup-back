#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS A1

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors (&oneWire);
void setup() {

Serial.begin(9600);

sensors.begin();
}
void loop() {

sensors.requestTemperatures();

float tempC = sensors.getTempCByIndex(0); // index 0 refers to the first device

float tempF = sensors.getTempFByIndex(0);

Serial.print("Il fait :");
Serial.print (tempC);
Serial.print("°");
  // Wait 1 second:
delay(1000);
}
