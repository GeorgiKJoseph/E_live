const int RelayPin = 3;

void setup() {
  Serial.begin(9600);
  pinMode(RelayPin, OUTPUT);
}

void loop() {
  digitalWrite(RelayPin, HIGH);
  delay(3000);
  digitalWrite(RelayPin, LOW);
  delay(3000); 
}
