import datetime
import time
import flask
from flask_pymongo import PyMongo

app = flask.Flask(__name__)

class database:
    def __init__(self):
        app.config['MONGO_URI'] = 'mongodb://exceed_group10:3rgdvs6u@158.108.182.0:2255/exceed_group10'
        mongo = PyMongo(app)
        self.myCollection = mongo.db.g10

    def find_one(self, type):
        filt = {'type': type}
        data = self.myCollection.find_one(filt)
        return {"data" : data}

    def insert(self, payload):
        self.myCollection.insert_one(payload)
        return {'result': 'Created successfully'}

    def update(self, type, pos, data):
        filt = {'type' : type}
        updated_content = {"$set": {pos : data}}
        self.myCollection.update_one(filt, updated_content)
        return {'result' : 'Updated successfully'}

def setZero(types):
    data = database().find_one(types)
    database().update(types, "water1", 0)
    database().update(types, "water2", 0)
    return {'result' : 'setZero successfully'}

def updatePopular(types):
    data = database().find_one(types)
    popularwater = ""
    if data["data"]["water1"] > data["data"]["water2"]:
        popularwater = "water1"
    elif data["data"]["water1"] < data["data"]["water2"]:
        popularwater = "water2"
    else: #equal
        popularwater = "draw"
    print("water1 = "+str(data["data"]["water1"]))
    print("water2 = "+str(data["data"]["water2"]))
    print("popularwater is " + popularwater)
    database().update(types, "popularwater", popularwater)
    return {'result' : 'Updated successfully'}

def hourStatistics():
    timestamp = datetime.datetime.now().hour
    time = str(datetime.time(timestamp - 1, 0, 0))
    date = str(datetime.datetime.now().date())
    time_stat = date + " " + time
    payload = database().find_one("statistics")["data"]
    payload = {
        "water1": database().find_one("hoursPopular")["data"]["water1"],
        "water2": database().find_one("hoursPopular")["data"]["water2"]
    }
    database().update("statistics", time_stat, payload)

now = datetime.datetime.now()
now_minute = 60 - now.minute
now_second = 60 - now.second
now_micro = 1000000 - now.microsecond
if now_minute == 60 and now_second == 60 and now_micro == 1000000:
    now_minute = 0
    now_secound = 0
    now_micro = 0

if now_micro < 1000000: #check microsecond
    now_second -= 1
else:hou
    now_micro = 0

if now_second < 60: #check second
    now_minute -= 1
else:
    now_second = 0
#time.sleep(now_minute*60 + now_second + now_micro*(10**-6))
Time_sleep = now_minute*60 + now_second + now_micro*(10**-6)
print("Sleep " + str(Time_sleep) + " second(s)")
time.sleep(Time_sleep)


while True:
    now = datetime.datetime.now()
    #print(now)
    updatePopular("hoursPopular")
    hourStatistics()
    #time.sleep(0.5)
    #now = datetime.datetime.now()
    #print(now)
    setZero("hoursPopular")
    print("Reset hoursPopular.. (" + str((now.hour-1)%24) + ":00 - " + str(now.hour%24) + ":00)")
    print(now)
    if now.hour == 0: #Everyday
        updatePopular("dayPopular")
        # Update data here
        #time.sleep(0.5)
        setZero("dayPopular")
        print("Reset dayPopular..")
        if now.weekday() == 6: #Sunday (Every week)
            updatePopular("weekPopular")
            #time.sleep(0.5)
            setZero("weekPopular")
            print("Reset weekPopular..")

    now_minute = 60 - now.minute
    now_second = 60 - now.second
    now_micro = 1000000 - now.microsecond

    if now_micro < 1000000: #check microsecond
        now_second -= 1
    else:
        now_micro = 0

    if now_second < 60:
        now_minute -= 1
    else:
        now_second = 0
    Time_sleep = now_minute*60 + now_second + now_micro*(10**-6)
    print("Sleep " + str(Time_sleep) + " second(s)")
    time.sleep(Time_sleep)
