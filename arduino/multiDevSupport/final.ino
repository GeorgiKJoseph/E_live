// Using Protothreading
#include<TimedAction.h>
// L :- LED  S:- switch  R:- relay
// relay module is active low
#define low HIGH
#define high LOW

// Device 1
#define Dev1_R 2
#define Dev1_S 3
#define Dev1_L 4
// Device 2
#define Dev2_R 5
#define Dev2_S 6
#define Dev2_L 7
// Device 3
#define Dev3_R 8
#define Dev3_S 9
#define Dev3_L 10
// Device 4
#define Dev4_R 11
#define Dev4_S 12
#define Dev4_L 13

// analog input from gate effect sensor ACS712
#define gateIn A0

// variable for calculating instant power
double Voltage = 0;
double VRMS = 0;
double AmpsRMS = 0;
int mVperAmp = 66;

// function prototype
void switch1Listen();
void switch2Listen();
void switch3Listen();
void switch4Listen();
void ledControl(int, boolean);
void getInstantPower();
float getVPP();

// setting Protothreads to Listen to switches
TimedAction Lis1Thread = TimedAction(100,switch1Listen);
TimedAction Lis2Thread = TimedAction(100,switch2Listen);
TimedAction Lis3Thread = TimedAction(100,switch3Listen);
TimedAction Lis4Thread = TimedAction(100,switch4Listen);
// setting Protothread to calculate InstantPower in every 5sec
TimedAction InstanPowThread = TimedAction(1000,getInstantPower);

// Device on/off status
boolean D1_STATUS = false;
boolean D2_STATUS = false;
boolean D3_STATUS = false;
boolean D4_STATUS = false;


void setup() {
  // baud rate:- 9600 (9600bits per sec)
  Serial.begin(9600);
  // Setting pinMode()
  // Device 1
  pinMode(Dev1_R, OUTPUT);
  pinMode(Dev1_L, OUTPUT);
  // Device 2
  pinMode(Dev2_R, OUTPUT);
  pinMode(Dev2_L, OUTPUT);
  // Device 3
  pinMode(Dev3_R, OUTPUT);
  pinMode(Dev3_L, OUTPUT);
  // Device 3
  pinMode(Dev4_R, OUTPUT);
  pinMode(Dev4_L, OUTPUT);

  int i = 0;
  // setting all output pins to low
  for(i=2;i<=13;i++) {
    //initializing relay pins to low
    digitalWrite(i++,low);
    // initializing LED pins to low
    digitalWrite(++i,LOW);
  }
}

void loop() {
  // Switch Listener
  Lis1Thread.check();
  Lis2Thread.check();
  Lis3Thread.check();
  Lis4Thread.check();
  // Calculate Instant power
  InstanPowThread.check();
}

// shift led state paras(pinNo, T/F)
void ledControl(int ledNo, boolean state) {
  digitalWrite(ledNo,state);
}

// Shift relay state paras(relayNo,T/F)
void relayControl(int relayNo, boolean state) {
  // relays are active low
  state ? state = false : state = true;
  digitalWrite(relayNo,state);
}

// Protothread to Listen to switch1
void switch1Listen() {
  // Switch instant status
  boolean s1;
  s1 = digitalRead(Dev1_S);
  // Changing state
  if(s1 == false) {
    D1_STATUS ? D1_STATUS = false : D1_STATUS = true;
    if (D1_STATUS){
      Serial.write("Device1 ON\n");
    } else {
      Serial.write("Device1 OFF\n");
    }

    // Changing led state
    ledControl(Dev1_L,D1_STATUS);
    // Changing relay state
    relayControl(Dev1_R,D1_STATUS);

    // Switch 1 semaphore
    while (s1 == 0)
      s1 = digitalRead(Dev1_S);
  }
}

// Protothread to Listen to switch2
void switch2Listen() {
  // Switch instant status
  boolean s2;
  s2 = digitalRead(Dev2_S);
  // Changing state
  if(s2 == false) {
    D2_STATUS ? D2_STATUS = false : D2_STATUS = true;
    if (D2_STATUS){
      Serial.write("Device2 ON\n");
    } else {
      Serial.write("Device2 OFF\n");
    }

    // Changing led state
    ledControl(Dev2_L,D2_STATUS);
    // Changing relay state
    relayControl(Dev2_R,D2_STATUS);

    // Switch 2 semaphore
    while (s2 == 0)
      s2 = digitalRead(Dev2_S);
  }
}

// Protothread to Listen to switch3
void switch3Listen() {
  // Switch instant status
  boolean s3;
  s3 = digitalRead(Dev3_S);
  // Changing state
  if(s3 == false) {
    D3_STATUS ? D3_STATUS = false : D3_STATUS = true;
    if (D3_STATUS){
      Serial.write("Device3 ON\n");
    } else {
      Serial.write("Device4 OFF\n");
    }

    // Changing led state
    ledControl(Dev3_L,D3_STATUS);
    // Changing relay state
    relayControl(Dev3_R,D3_STATUS);

    // Switch 3 semaphore
    while (s3 == 0)
      s3 = digitalRead(Dev3_S);
  }
}

// Protothread to Listen to switch4
void switch4Listen() {
  // Switch instant status
  boolean s4;
  s4 = digitalRead(Dev4_S);
  // Changing state
  if(s4 == false) {
    D4_STATUS ? D4_STATUS = false : D4_STATUS = true;
    if (D4_STATUS){
      Serial.write("Device4 ON\n");
    } else {
      Serial.write("Device4 OFF\n");
    }

    // Changing led state
    ledControl(Dev4_L,D4_STATUS);
    // Changing relay state
    relayControl(Dev4_R,D4_STATUS);

    // Switch 4 semaphore
    while (s4 == 0)
      s4 = digitalRead(Dev4_S);
  }
}

// Calculates total power
void getInstantPower() {
  Voltage = getVPP();
  VRMS = (Voltage/2.0) *0.707;  //root 2 is 0.707
  AmpsRMS = (VRMS * 1000)/mVperAmp;
  Serial.println(AmpsRMS-0.12);
}

// Returns voltage
float getVPP()
{
  float result;
  int readValue,i=0;             //value read from the sensor
  int maxValue = 0;          // store max value here
  int minValue = 1024;

  while(i<3000)
   {
       readValue = analogRead(gateIn);
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
       i++;
   }

   // Subtract min from max
   result = ((maxValue - minValue) * 5.0)/1024.0;
   Serial.print("Raw: ");
   Serial.println(result);
   return result;
 }
