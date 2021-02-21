# exceedProject_G10
The topic is "IOT for new normal" so our group decides to do a water dispenser. this idea based on the "contactless" concept 

### HARDWARE

### BACKEND
In the backend part, we use the Flask framework to manage the Raspberry pi based server. the server gets a response from hardware(esp32 microcontroller), it will be calculating water left, time interval, and the usage statistic in a time interval and update data to MongoDB database the frontend will fetching the data through "/popular path" to access to a database and hardware will using GET and POST method to communicate with the server through "/water" path.

-to run a server
```shell
python3 app.py 
```
-to run a time reset function
```shell
python3 timeDivider.py
```

### FRONTEND

There is a single page homepage that shows the status of the water dispenser, there will be animation while opening the website for 5 seconds with cool tone colors. Comfortable for the user Program written: HTML + CSS + JAVASCRIPT, the following sections are explained in detail.

มีหน้าเดียวคือ homepage แสดงสถานะต่าง ๆ ของตู้กดน้ำ โดยจะมี Animation ขณะเปิดหน้าเว็บไซต์ 5 วินาที มีสีสันออกไปทางโทนเย็น
สบายตาต่อผู้ใช้ โปรแกรมที่ใช้เขียน : HTML + CSS + JAVASCRIPT จะอธิบายรายละเอียดส่วนต่าง ๆ ดังต่อไปนี้

Navigation bar:
Home page - go to the main page
Department of Disease Control - shortcut for checking news about the virus(linking to Department of Disease Control website).
Contact channel - the web page of the representative of the group for contacting
About - About this webpage
refresh-icon - Show the rotation status if the website has fetched complete information if it not done will stop spinning
stat-icon - shows the current state of the water for each tank as a percentage.

Navigation bar:
หน้าหลัก - ไปยังหน้าหลัก
กรมควบคุมโรค - shortcut สำหรับเชคข่าวสารเกี่ยวกับเชื้อไวรัส
ช่องทางติดต่อ - เว็ปเพจของตัวแทนของกลุ่มสำหรับติดต่อ
เกี่ยวกับ - เกี่ยวกับเว็บเพจนี้ -w-
refresh-icon - แสดงสถานะหมุนถ้าเว็ปไซต์สามารถ fetch ข้อมูลได้ครบถ้วน ถ้าไม่ครบจะหยุดหมุน
stat-icon - แสดงสถานะน้ำแต่ละ tank เหลืออยู่ ณ ปัจจุบันเป็นเปอร์เซนต์

Left Column: 
  KU Smart Water - Name of this Project 
  Slogan - For entertainment only 
  Left bottom picture - If user have no idea what to drink so they can watch here for recommendation. Program will randomize the picture while open this website or having 
                        someone dispense water. 
  Description - Recommendation for safety.

Left Column: 
  KU Smart Water - ไอคอนของ Project 
  Slogan - เพื่อความบันเทิง 
  รูปภาพด้านล่างซ้าย - ถ้าคนกดน้ำนึกไม่ออกว่าจะกินน้ำอะไรสามารถดูการแนะนำตรงนี้ได้ โดยโปรแกรมจะทำการสุ่มครั้งแรกขณะเริ่มต้นเวปไซต์และสุ่มใหม่หลังจากมีการกดน้ำ 
  คำอธิบาย - เชิญชวนให้ป้องกันเชื้อไวรัส

Fetching data every 5 seconds, This interval value close to average of dispensing water duration and don't let the server have too much data loading. 
Fetching data will fetch the remaining water, Dispenser count in present and last dispensse count for hour day and week.

// การ Fetch จะทำทุก ๆ 5 วินาทีซึ่งจะใกล้เคียงกับค่าเฉลี่ยในการกดน้ำ 1 ครั้งและไม่ให้ Server ทำงานหนักจนเกินไป // การ Fetch จะทำการดึงข้อมูลน้ำที่เหลิออยู่ จำนวนการกดน้ำช่วงปัจจุบันและน้ำที่มีการกดมากที่สุดในช่วงที่ผ่านมา ได้แก่ ระดับชั่วโมง ระดับวัน และ ระดับสัปดาห์

Middle column: Show current dispenser count from starting new hour (XX:00) to last minute in this hour (XX:59). If start new hour the program will display the most popular   
               drink. And have the bar to display time. 
 
Middle Column: แสดงข้อมูลการกดน้ำ ณ ปัจจุบัน ตั้งแต่เริ่มชั่วโมงใหม่จนถึงเวลาสิ้นสุดชั่วโมงนั้น โดยมีเวลากำกับไว้ด้านล่าง เมื่อเริ่มต้น ชั่วโมงใหม่จะแสดงผลน้ำที่มีการกดมากที่สุดเป็นหมายเลขตู้

Right Column: Similar to the middle column. Show current dispenser count from starting new day (00:00; GMT0) and week (Sunday) to last of each time interval.
              If start next day or next week the program will display the most popular drink to the each section.

Right Column: จะแสดงผลคล้าย ๆ กับ Middle Column ก็คือ แสดงข้อมูลการกดน้ำ ณ ปัจจุบันตั้งแต่เริ่มต้นวันใหม่(เที่ยงคืน)และสัปดาห์ใหม่(วันอาทิตย์) จนถึงสิ้นสุดของช่วงเวลานั้น เมื่อเริ่มต้นใหม่จะแสดงผลน้ำที่มีการกดมากที่สุดเป็นหมายเลขตู้ 
