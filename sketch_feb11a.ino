int pirPin = 3;   // PIR sensor pin
int ledPin = 13;  // LED pin

int motionCounter = 0;  
const int motionThreshold = 3;  // Allows small sensitivity filtering

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(pirPin) == HIGH) {
    motionCounter++;  
    Serial.print("Motion detected! Count: ");
    Serial.println(motionCounter);
    delay(100);  // Small delay to prevent rapid false triggers
  } else {
    motionCounter = 0;  // Reset if no motion
  }

  if (motionCounter >= motionThreshold) {  
    Serial.println("🚨 INTRUDER ALERT! 🚨");
    digitalWrite(ledPin, HIGH);  
    delay(5000);  // LED stays on for 5 seconds
    digitalWrite(ledPin, LOW);
    motionCounter = 0;  
  }
}