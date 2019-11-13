const int LEDPin = 5 ;
const int SwitchPin = 4;
const int RelayPin = 3;
const int sensorIn = A0;
int d=0;
int status =0;
int incomingByte;
int mVperAmp = 66; 
double Voltage = 0;
double VRMS = 0;
double AmpsRMS = 0;
void setup() {
  Serial.begin(9600);
  pinMode(LEDPin, OUTPUT);
  pinMode(SwitchPin, INPUT);
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, HIGH);
}

//RelayPin = LOW = bulb_on

void loop() {
  Voltage = getVPP();
  VRMS = (Voltage/2.0) *0.707;  //root 2 is 0.707
  AmpsRMS = (VRMS * 1000)/mVperAmp;
  //Serial.println("C");
  Serial.println(AmpsRMS-0.12);
  //Serial.println(" Amps RMS");
  
  if(Serial.available() > 0){
    incomingByte = Serial.read();
    if(incomingByte == 'H'){
      status = 0;
      //digitalWrite(LEDPin,LOW);
      //digitalWrite(RelayPin, LOW);
    }
    else if(incomingByte == 'L'){
      status = 1;
      //digitalWrite(LEDPin,HIGH);
      //digitalWrite(RelayPin, HIGH);
    }
  }
  d=digitalRead(SwitchPin);
  if (d==0){
    if(status ==1){
      status = 0;
      Serial.write("F");
    }else{
      status =1;
      Serial.write("O");
    }
    Serial.write("\n");
    
  }
  if (status==1){
    digitalWrite(LEDPin,HIGH);
    digitalWrite(RelayPin, LOW);
  }else if(status==0){
    digitalWrite(LEDPin,LOW);
    digitalWrite(RelayPin, HIGH);
  }
  while(d==0)
    d=digitalRead(SwitchPin);
  delay(10);
}
float getVPP()
{
  float result;
  int readValue,i=0;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;          // store min value here
  
   uint32_t start_time = millis();
   //while((millis()-start_time) < 3000) //sample for 3 Sec
   while(i<3000)
   {
       readValue = analogRead(sensorIn);
       // see if you have a new maxValue
       if (readValue > maxValue) 
       {
           /*record the maximum sensor value*/
           maxValue = readValue;
       }
       if (readValue < minValue) 
       {
           /*record the minimum sensor value*/
           minValue = readValue;
       }
       i+=1;
   }
   
   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024.0;   
   return result;
 }