import paho.mqtt.client as mqtt
import time 
import json
from hal import *

with open ("payload.json") as payload:
    definition = json.load(payload)

for definitions in definition:
    USER = definition.get("payload").get("client").get("user")
    PASSWORD = definition.get("payload").get("client").get("password")
    CLIENT_ID = definition.get("payload").get("client").get("client_id")
    SERVER = definition.get("payload").get("client").get("server")
    PORT = definition.get("payload").get("client").get("port")
    #checar a temperatura inicial da fazenda.
    fazenda1_temperatura = definition.get("payload").get("fazenda1").get("temperatura_inicial")

client = mqtt.Client(CLIENT_ID)
client.username_pw_set(USER, PASSWORD)
client.connect(SERVER, PORT)

def message(client, userdata, msg):
    vetor = msg.payload.decode().split(",")
    aquecedor("on" if vetor[1] == "1" else "off")
    client.publish(f"v1/{USER}/things/{CLIENT_ID}/response", f"ok,{vetor[0]}")
    return print(vetor)

#*Subscriber
client.on_message = message
client.subscribe(f"v1/{USER}/things/{CLIENT_ID}/cmd/2")
client.loop_start()

#*Publiser
while True:       
    client.publish(f"v1/{USER}/things/{CLIENT_ID}/data/0", umidade())  
    client.publish(f"v1/{USER}/things/{CLIENT_ID}/data/1", temperatura(fazenda1_temperatura))
    time.sleep(5)

client.disconnect()
