import flask
import requests
import json
import datetime
from flask_pymongo import PyMongo
from flask_cors import CORS,cross_origin


app = flask.Flask(__name__)
cor = CORS(app)

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

def getInterval(num):
    status = database().find_one(f"status{num}")
    time = status["data"]["timestamp"]
    timestamp = datetime.datetime.now() + datetime.timedelta(hours=7)
    return timestamp - time

def settime(num):
    timestamp = datetime.datetime.now() + datetime.timedelta(hours=7)
    database().update(f"status{num}", "timestamp", timestamp)
    return f"set time of status{num} to {timestamp}"

def waterleft(num, time):
    # Q = V/t
    # container is crystal water bottle 600 ml
    # After experiment it takes up to 6 second that water flow out of 600 ml container
    # mean that in 1 second water flow 100 ml
    containerVolume = 1500
    currentVolume = containerVolume * (database().find_one("volume")["data"][f"water{num}"] / 100)
    q = 50
    leftVolume = currentVolume - (q * time)
    if leftVolume < 0:
        leftVolume = 0
    percentageLeft = int((leftVolume * 100) / containerVolume)
    database().update("volume", f"water{num}", percentageLeft)
    return f"container{num} has {percentageLeft} % "

def refill(num):
    database().update("volume", f"water{num}", 100)
    return f"refill container{num}"

def upInterval(num):
    interval = getInterval(num)
    print(waterleft(num, interval.total_seconds()))
    interval = str(interval)
    data = database().find_one("intervalData")["data"][f"status{num}"]
    data.append(interval)
    database().update("intervalData", f"status{num}", data)
    return f"append interval to status{num}"

def updatePopular(num):
    data = database().find_one("hoursPopular")
    amount = data["data"][f"water{num}"]
    database().update("hoursPopular", f"water{num}", amount + 1)
    data = database().find_one("dayPopular")
    amount = data["data"][f"water{num}"]
    database().update("dayPopular", f"water{num}", amount + 1)
    data = database().find_one("weekPopular")
    amount = data["data"][f"water{num}"]
    database().update("weekPopular", f"water{num}", amount + 1)
    return "popular updated"

def isEmpty(num):
    data = database().find_one("volume")["data"][f"water{num}"]
    if data >= 20:
        return 1
    return 0

@app.route('/')
@cross_origin()
def hello():
    return "Hello world",200

@app.route('/water', methods=['POST', 'GET'])
@cross_origin()
def water():
    if flask.request.method == 'POST':
        # POST method
        payload = flask.request.data.decode()
        print(f"payload : {payload}")
        if payload != "null" and payload != None:
            payload = json.loads(payload)
            data= {}
            for k,v in payload.items():
                if k == "fill1":
                    if payload["fill1"] == 1:
                        print(refill(1))
                        return f"refill 1"
                    else:
                        return "good"
                elif k == "fill2":
                    if payload["fill2"] == 1:
                        print(refill(2))
                        return f"refill 2"
                    else:
                        return "good"
                if k == "ldr1" or k == "ultrasonic1":
                    if payload["ldr1"] == 1 and payload["ultrasonic1"] == 1:
                        database().update("lastUsage", "status1", 1)
                        print(settime(1))
                        return {"status1" : isEmpty(1), "status2" : isEmpty(2)}
                    elif (payload["ldr1"] == 0 or payload["ultrasonic1"] == 0) and database().find_one("lastUsage")["data"]["status1"]:
                        database().update("lastUsage", "status1", 0)
                        print(upInterval(1))
                        print(updatePopular(1))
                        return {"status1" : isEmpty(1), "status2" : isEmpty(2)}
                    else:
                        return {"status" : "looking good ;)"}
                else:
                    if payload["ldr2"] == 1 and payload["ultrasonic2"] == 1:
                        database().update("lastUsage", "status2", 1)
                        print(settime(2))
                        return {"status1" : isEmpty(1), "status2" : isEmpty(2)}
                    elif (payload["ldr2"] == 0 or payload["ultrasonic2"] == 0) and database().find_one("lastUsage")["data"]["status2"]:
                        database().update("lastUsage", "status2", 0)
                        print(upInterval(2))
                        print(updatePopular(2))
                        return {"status1" : isEmpty(1), "status2" : isEmpty(2)}
                    else:
                        return {"status" : "looking good ;)"}

            timestamp =  datetime.datetime.now() + datetime.timedelta(hours = 7)
            data["timestamp"] = timestamp
            print(f"data :  {data}")
            #database().insert(data)
            return "method POST", 200
    elif flask.request.method == 'GET':
        # GET method
        payload = flask.request.data.decode()
        print(payload)
        return {"status1" : isEmpty(1), "status2" : isEmpty(2)}, 200

    else:
        flask.abort(400)

@app.route('/popular', methods=['GET'])
def find():
    types = flask.request.args.get('Type')
    query = database().find_one(types)
    payload = {}
    payload["type"] = query["data"]["type"]
    payload["popularwater"] = query["data"]["popularwater"]
    payload["water1"] = query["data"]["water1"]
    payload["water2"] = query["data"]["water2"]
    return payload
    #return {'result': query["data"]["popularwater"]}

@app.route('/volume', methods=['GET'])
def update_volume():
    query = database().find_one("volume")
    payload = {}
    payload["water1"] = query["data"]["water1"]
    payload["water2"] = query["data"]["water2"]
    return payload


if __name__ == "__main__":
    app.run(debug=True, port=3000, host='158.108.182.12')
