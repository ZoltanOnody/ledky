#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <ESP8266WebServer.h>
const size_t capacity = JSON_OBJECT_SIZE(16) + 60;
DynamicJsonDocument document(capacity);


Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

ESP8266WebServer server(80);

const char* ssid = "JaJ";
const char* password = "achjajanisanepytaj";
void handleLed() {
      if (server.hasArg("plain")== false){ //Check if body received
 
            server.send(200, "text/plain", "Body not received");
            return;
 
      }
 
      String message = "Body received:\n";
             message += server.arg("plain");
             message += "\n";
  
      server.send(200, "text/plain", message);
  deserializeJson(document, server.arg("plain"));
  JsonObject root = document.as<JsonObject>(); 
  for (int i=0; i<=15; i++) {
    String y = String(i);
//    Serial.print("y = ");
//    Serial.println(y);
    Serial.println("led"+y);
    if (root.containsKey("led"+y)) {
//      const char* value = root["led"+y];
      int value = root["led"+y];
      Serial.print("value = ");
      Serial.println(value);
      pwm.setPWM(i, 0, value);       
    }    
  }
  if (root.containsKey("PWMfreq")) {
    int freq = root["PWMfreq"];
    pwm.setPWMFreq(freq);
  }
  Serial.println(server.arg("plain"));
 }
void setup() {
  // Setup serial-output
  Serial.begin(115200);
  delay(10);
  pwm.begin();
  pwm.setPWMFreq(1600);  // This is the maximum PWM frequency

  boot_setup();
  WiFi.mode(WIFI_STA);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Set the hostname
  WiFi.hostname("ledky-web-esp8266");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");

 
  server.on("/led", handleLed);
  server.begin();
  uint16_t color = 0;
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    WiFi.begin(ssid,password);
  }
  server.handleClient();

}
void boot_setup() {
  pwm.setPWM(0,0,1000);
  pwm.setPWM(1,0,600);
  pwm.setPWM(2,0,400);
}
