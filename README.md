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


## demo picture
<img src="https://women.mthai.com/app/uploads/2019/08/content_HotelDelLuna41-1.jpg", alt=""IU>
