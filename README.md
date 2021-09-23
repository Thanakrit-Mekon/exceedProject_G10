# exceedProject_G10
The topic is "IOT for new normal" so our group decides to do a water dispenser. this idea based on the "contactless" concept 

## BACKEND
In the backend part, we use the Flask framework to manage the Raspberry pi based server. the server gets a response from hardware(esp32 microcontroller), it will be calculating water left, time interval, and the usage statistic in a time interval and update data to MongoDB database the frontend will fetching the data through "/popular path" to access to a database and hardware will using GET and POST method to communicate with the server through "/water" path.

## to run a server
```shell
python3 app.py 
```
## to run a time reset function
```shell
python3 timeDivider.py
```

## FRONTEND

There is a single page homepage that shows the status of the water dispenser, there will be animation while opening the website for 5 seconds with cool tone colors. Comfortable for the user Program written: HTML + CSS + JAVASCRIPT, the following sections are explained in detail.

### Navigation bar:
Home page - go to the main page
Department of Disease Control - shortcut for checking news about the virus(linking to Department of Disease Control website).
Contact channel - the web page of the representative of the group for contacting
About - About this webpage
refresh-icon - Show the rotation status if the website has fetched complete information if it not done will stop spinning
stat-icon - shows the current state of the water for each tank as a percentage.

### Left Column: 
  KU Smart Water - Name of this Project 
  Slogan - For entertainment only 
  Left bottom picture - If user have no idea what to drink so they can watch here for recommendation. Program will randomize the picture while open this website or having someone dispense water. 
  Description - Recommendation for safety.

Fetching data every 5 seconds, This interval value close to average of dispensing water duration and don't let the server have too much data loading. 
Fetching data will fetch the remaining water, Dispenser count in present and last dispensse count for hour day and week.

### Middle column: 
Show current dispenser count from starting new hour (XX:00) to last minute in this hour (XX:59). If start new hour the program will display the most popular   
drink. And have the bar to display time. 
 
### Right Column: 
Similar to the middle column. Show current dispenser count from starting new day (00:00; GMT0) and week (Sunday) to last of each time interval.
If start next day or next week the program will display the most popular drink to the each section.

## HARDWARE
Arduino code for ultrasonic ldr led and servo controling 

### ultrasonic
An ultrasonic sensor is a type of electronic equipment that emits ultrasonic sound waves and transforms the reflected sound into an electrical signal to determine the distance of a target item and in our product, we utilize ultrasonic to detect those who attempt to press water without touching it.

### led
A light-emitting diode (LED) is a semiconductor light source that emits light when current is sent through it. Identify whether or not there is water in the tank

### ldr
An LDR (Light Dependent Resistor) is a component with a resistance that varies with the amount of light that strikes it. As a result, they may be utilized in light sensor circuits and we utilize ldr in two places: first, in the orange area to fill the water, and second, on the cup holder to inform the machine that the cup is ready for water pouring.

### servomotor
A servomotor is a rotary or linear actuator that enables precise control of angular or linear position, velocity, and acceleration.  It comprises of a suitable motor connected to a position feedback sensor.When there is a cup in the cup holder and the ultrasonic is blocked, open the tank's cover.

## Demonstrate VDO
https://youtu.be/DgLNCGfBTYo

## Presentation VDO (1:13:17 - 1:36:30)
https://www.youtube.com/watch?v=ZgWhyuSs5_s&ab_channel=%E0%B8%9B%E0%B9%8B%E0%B8%B2%E0%B8%9E%E0%B8%B2%E0%B8%94%E0%B8%B4%E0%B8%9FOfficial

## group picture
![image](https://user-images.githubusercontent.com/63298507/134477084-a879cae2-4507-4077-a1ee-b85d68121c93.png)

## Demo picture
![Picture](https://github.com/Thanakrit-Mekon/exceedProject_G10/blob/main/g10.jpg?raw=true)

## Group members
Phumrapee Chaowanapricha 6210546692   
Bheem Suttipong 6210546005   
Suchon Prasert 6210545637     
Thanakrit Mek-on 6210500129   
Phakinee Sirisukpoca 6210503748   
Sirapat Inchan 6210503888   
Thitisak Siratchatamatawin 6210503551   
Chaiyo Churngam 6210503543    




