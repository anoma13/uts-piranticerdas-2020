const int trigPin = D4;
const int echoPin = D3;
int incomingByte = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  long micro, milli, second, cm;
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);

  //waktu tempuh
  micro = pulseIn(echoPin, HIGH);
  milli = micro / 1000;
  //jarak yang ditempuh
  cm = micro * 0.034 / 2;

  Serial.print(cm);
  Serial.print(";");
  Serial.print(micro);
  Serial.print(";");
  Serial.println(milli);
  delay(100);

    if(Serial.available() > 0){
    incomingByte = Serial.read();
    if (incomingByte!=97){
      return;
    }else{
        digitalWrite(D4, HIGH);   
        delay(100);                    
        digitalWrite(D4, LOW);  
        delay(100);   
    }
  }

}
