

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(A1, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A1);

  int pourcentage = map(sensorValue,0,650,0,100);
  
  Serial.print("Hum.Sol = ");
  Serial.print(pourcentage);
  Serial.print(" % ");
  delay(5000);        // delay in between reads for stability
}
