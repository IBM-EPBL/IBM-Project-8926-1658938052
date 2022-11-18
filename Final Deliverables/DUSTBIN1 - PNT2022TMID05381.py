#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk
import time
import random
myConfig = {
    "identity": {
        "orgId": "nhpwjc",
        "typeId": "NodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token": "123456789"
    }
}
lat="13.167589"
lon="80.248510"
name="point1"
icon="fa-trash-o"
color="green"
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,100)
    if temp>60:
        icon="fa-trash"
        color = "red"
    else:
        icon = "fa-trash-o"
        color = "green"
    myData={"Name":name,"Latitude":lat,"Longitude":lon,"Icon":icon,"FillPercent":temp,"Color":color}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(10)
client.disconnect()
