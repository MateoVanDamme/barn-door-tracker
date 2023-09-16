  /* 
   *  Chip: Trinket M0
   *  Controls the stepper motor that turns the telescope platform while correcting for sinus error. 
   *  Explanation of the variables:
   *  delta0:   correct timing for t = 0 sec (in ms)
   *  delta:    calculated time for t > 0 (in ms)
   *  w0:        rotational speed of the earth in rad/s
   *  For a history of used delta0 values see: "Log values.xlsx" 
   *  Speed last changed 23 december 2021
   */

//These change depending on tracker design and motor
const int pinStep = 2;
const int pinDir = 0;
const float delta0 = 207.0;

//These variables stay the same even for different motors and trackers
const float w0 = 2.0*PI/ 86164.0;

float delta = delta0;
unsigned long time_last = 0;
bool toggle = false;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pinStep, OUTPUT);
  pinMode(pinDir,OUTPUT);

  digitalWrite(pinDir, HIGH);
}

void loop() {  
  if(micros() - time_last > delta){
    //toggle output pin first
    toggle = !toggle;
    digitalWrite(LED_BUILTIN, toggle);  
    digitalWrite(pinStep,toggle);    
    time_last = micros();

    //Now we have ~50ms to calculate the new delta
    delta = delta0 /(cos(w0*(float)millis()/2000.0));
    //To micros from millis
    delta = delta*1000.0;
    //2 because we step only once per 2 deltas
    delta/=2.0;            
    }      
}
