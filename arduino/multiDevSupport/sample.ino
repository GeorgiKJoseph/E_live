// Using Protothreading
#include<TimedAction.h>
// L :- LED  S:- switch  R:- relay
// relay module is active low
#define high LOW
#define low HIGH

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

// function prototype
void BlinkLed1();

// setting Protothreads to execute following functions with a delay 1000ms 500 250 125
TimedAction Blink1 = TimedAction(10,BlinkLed1);

// Led state testing variables
boolean l1 = false;
boolean l2 = false;
boolean l3 = false;
boolean l4 = false;


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
  for(i=2;i<=13;i+2) {
    //initializing relay pins to low
    digitalWrite(i++,low);
    // initializing LED pins to low
    digitalWrite(i,LOW);
  }
}

void loop() {
  //Blink1.check();
}

// BlinkLed1() definition
void BlinkLed1() {
  strtng:
    digitalWrite(Dev1_L,HIGH);
    delay(500);
    digitalWrite(Dev1_L,LOW);
    delay(500);
    goto strtng;
}
