import time
import os
import subprocess
import paho.mqtt.client as mqtt
import json

# "192.168.88.241"
broker_address="192.168.88.241" 
mqtt_topic="Pure"

def on_message(client, userdata, message):
#     print("message received " ,str(message.payload.decode("utf-8")))
#     print("message topic=",message.topic)
#     print("message qos=",message.qos)
#     print("message retain flag=",message.retain)   
#     playSingleShot()
    obj = str(message.payload.decode("utf-8"))    
#     val = obj
    print(obj)
    send2Pd(obj)


def send2Pd(message=''):
        f = open("sensors.txt","w+") 
        f.write(message)
        f.close() 
        print("write!")
        os.system("echo '" + message + "' | /Applications/Pd-0.49-1.app/Contents/Resources/bin/pdsend 3001 localhost udp")


print("creating new mqtt client instance")
client = mqtt.Client("PureData")

print("connecting to broker")
client.connect(broker_address, 1883)

print("Subscribing to topic",mqtt_topic)
client.subscribe(mqtt_topic)

print("Publishing message to topic",mqtt_topic)
#client.publish(mqtt_topic,"Hallo!!!")

client.on_message=on_message
client.loop_start()

while True:
        print(".")
        #client.publish(mqtt_topic,"Hallo!!!")
        time.sleep(3)
