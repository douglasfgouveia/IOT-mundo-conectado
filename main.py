import paho.mqtt.client as mqtt
import time 
import json
from hal import *

# client = mqtt.Client(p)

with open ("payload.json") as payload:
    definition = json.load(payload)

def message(client, user, msg):
    if msg.topic == "pucpr/iotmc/fazenda/Aquecedor":
        aquecedor(msg.payload.decode()) 

client = mqtt.Client(definition.get("payload").get("client").get("client_id"))

client.username_pw_set(definition.get("payload").get("client").get("user"),
                       definition.get("payload").get("client").get("password"))
client.connect(definition.get("payload").get("client").get("SERVER"),
               definition.get("payload").get("client").get("PORT"))
client.on_message = message
client.subscribe('pucpr/iotmc/fazenda/#')
client.loop_start()

n=0
while n< 15: 

    client.publish(definition.get("payload").get("publish").get("topic"), 
                   umidade())
                #definition.get("payload").get("publish").get("message"))
    time.sleep(5)
    n+=1

client.disconnect()
