#include <Ultrasonic.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <ESP32Servo.h>


const char* ssid = "BBBBBBBB";
const char* password = "3422789789";
const char* url = "http://158.108.182.12:3000/water";


int rotating=0;
int state_ultrasonic=0;
int lastState_ultrasonic=0;
char str[50];
int ldr=34;
int state_ldr=0;
int lastState_ldr=0;
int which=0;
int servo = 32;
int status1 = 1 ; //1 = water , 0 = no waters
int status2 = 1 ;
//int LED2_R = 22;
int LED2_G = 23;
String payload;
int fill=0; // 1 = fill water , 0 = out of water
int ldr_fill = 33;


Servo myservo;
Ultrasonic ultrasonic(27);

const int _size = 2 * JSON_OBJECT_SIZE(3);
StaticJsonDocument<_size> JSONPost;
StaticJsonDocument<_size> JSONPost2;
StaticJsonDocument<_size> JSONGet;  

void WiFi_Connect() {
  WiFi.disconnect();
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to the WiFi network");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}


void _post(int which,int state) {  
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(url);
      http.addHeader("Content-Type", "appication/json");
      
        if(which == 1){
          JSONPost["ultrasonic2"] = state;
      }
        if(which == 2){
          JSONPost["ldr2"] = state;
      }
        serializeJson(JSONPost, str);
        int httpCode = http.POST(str);
        if (httpCode == HTTP_CODE_OK) {
          payload = http.getString();
          //Serial.println(httpCode);
          Serial.println(payload);
      }
      else {
        Serial.println(httpCode);
        Serial.println("ERROR on HTTP Request");
      }
    }
   
  
    else {
      WiFi_Connect();
    }
    delay(100);  

}

void _post2(int fill) {  
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(url);
      http.addHeader("Content-Type", "appication/json");
      
      JSONPost2["fill2"] = fill;
      
      serializeJson(JSONPost2, str);
      int httpCode = http.POST(str);
      if (httpCode == HTTP_CODE_OK) {
        payload = http.getString();
        //Serial.println(httpCode);
        Serial.println(payload);
      }
      else {
        Serial.println(httpCode);
        Serial.println("ERROR on HTTP Request");
      }
    }
   
  
    else {
      WiFi_Connect();
    }
    delay(100);  

}

void _get() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(url);
    int httpCode = http.GET();

    if(httpCode == HTTP_CODE_OK) {
      payload = http.getString();
      DeserializationError err = deserializeJson(JSONGet,payload);
      if (err) {
        Serial.print(F("deserializeJson() failed with code "));
        Serial.println(err.c_str());
        }
      else {
        /*
        Serial.println("check status ");
        Serial.println(httpCode);
        Serial.print("status1 : ");
        Serial.println((int)JSONGet["status1"]);
        Serial.print("status2 : ");
        Serial.println((int)JSONGet["status2"]);        
        */
        status1 = (int)JSONGet["status1"];
        status2 = (int)JSONGet["status2"];
        /*
        Serial.print("status1 : ");
        Serial.println(status1);
        Serial.print("status2 : ");
        Serial.println(status2);  
        */
        }
      }
    else {
      Serial.println(httpCode);
      Serial.println("ERROR on HTTP Request");
      }
    }
    else {
      WiFi_Connect();
      }
  }

 
void setup()
{
    pinMode(ldr,INPUT);
    pinMode(ldr_fill,INPUT);

    pinMode(LED2_G,OUTPUT);
   // pinMode(LED2_R,OUTPUT);
    
    myservo.attach(servo);
    digitalWrite(LED2_G,1);
    //digitalWrite(LED2_R,0);
    
    
    JSONPost["ultrasonic2"] = 0;
    JSONPost["ldr2"] = 0;
    JSONPost2["fill2"] = fill;

    //myservo.write(0);
    
    
    Serial.begin(9600);
    
}
void loop()
{  
    //fill water
    Serial.printf("ldr : %d\n",analogRead(ldr_fill));
    if(analogRead(ldr_fill) > 1400){
        fill = 1;  
        _post2(fill);
        status2 = 1;
    }

    //ULTRASONIC//
    long RangeInInches;
    long RangeInCentimeters;
  
    RangeInCentimeters = ultrasonic.MeasureInCentimeters(); // two measurements should keep an interval
    Serial.printf(">>>> %l\n", RangeInCentimeters);
    Serial.print("status1 : ");
    Serial.println(status1);
    Serial.print("status2 : ");
    Serial.println(status2);     
    
    digitalWrite(LED2_G,status2);
    //digitalWrite(LED2_R,!status2);
    if(lastState_ultrasonic == 0 && RangeInCentimeters <= 3 ){
        state_ultrasonic = 1;
        which = 1;
        _post(which,state_ultrasonic);
        
        Serial.print("ultranic2 ");
        Serial.println(state_ultrasonic);
        
    }
    if(lastState_ultrasonic == 1 && RangeInCentimeters > 3 ){
        state_ultrasonic  = 0;
        which = 1;
        _post(which,state_ultrasonic);
        
        Serial.print("ultranic2 ");
        Serial.println(state_ultrasonic);
        
    }
    delay(500);

    

    //LDR//
    Serial.println(analogRead(ldr));
    if(lastState_ldr == 0 && analogRead(ldr) > 2000 ){
        state_ldr = 1;
        which = 2;
        _post(which,state_ldr);
        
        Serial.print("ldr2");
        Serial.println(state_ldr);
        
    }
    if (lastState_ldr == 1 && analogRead(ldr) <= 2000 ){
        state_ldr = 0;  
        which = 2;
        _post(which,state_ldr);
        
        Serial.print("ldr2");
        Serial.println(state_ldr);
        
    }    
    delay(500);
    if(state_ldr == 1 ){
      if(lastState_ultrasonic == 0 && lastState_ldr == 1){
          
          Serial.println("in1");
          Serial.print(state_ldr);
          Serial.print(" ");
          Serial.println(state_ultrasonic );   
               
          if( state_ultrasonic == 1){
             if(rotating == 0){
                Serial.println("rotate1");
                myservo.write(0);
                delay(1000);
                //lastState_ldr = 0;
                //lastState_ultrasonic = 0;
                rotating = 1;
             }
          }  
        }
      
        if(lastState_ultrasonic == 1 && lastState_ldr == 1){  
            
            Serial.println("in2");
            Serial.print(state_ldr);
            Serial.print(" ");
            Serial.println(state_ultrasonic );
            
            if( state_ultrasonic == 0 ){ 
                if(rotating == 1){
                  Serial.println("rotate2");
                  myservo.write(180);  
                  delay(1000);
                  //lastState_ldr = 1;
                  //lastState_ultrasonic = 1;
                  rotating = 0;
                }
            }       
        }
      }
    lastState_ldr = state_ldr; 
    delay(500);
    lastState_ultrasonic = state_ultrasonic; 
    delay(500);
    fill = 0;
    _get();

}
