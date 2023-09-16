  // the setup function runs once when you press reset or power the board

int ledBuildtin  =13; 
int outputDirection = 0;
int outputStep = 2;
int delta = 50;

void setup() {
  // initialize pins
  pinMode(ledBuildtin, OUTPUT);
  pinMode(outputStep, OUTPUT);
  pinMode(outputDirection, OUTPUT);

  digitalWrite(outputDirection, LOW);

}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ledBuildtin, HIGH);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(outputStep,HIGH);
  delay(delta);              // wait for a second
  
  digitalWrite(ledBuildtin, LOW);    // turn the LED off by making the voltage LOW
  digitalWrite(outputStep,LOW);
  delay(delta);              // wait for a second
}
