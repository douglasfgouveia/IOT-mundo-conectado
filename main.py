
import paho.mqtt.client as mqtt
import time 
import json
from hal2 import *
from pubsub import * 

with open ("payload.json") as payload:
    definition = json.load(payload)

for definitions in definition:
    USER = definition.get("payload").get("client").get("user")
    PASSWORD = definition.get("payload").get("client").get("password")    
    SERVER = definition.get("payload").get("client").get("server")
    PORT = definition.get("payload").get("client").get("port")
    CLIENT1 = definition.get("payload").get("client").get("fazenda")
    CLIENT_ID_1 = definition.get("payload").get("client").get("client_id")
    CLIENT2 = CLIENT1 = definition.get("payload").get("client1").get("fazenda")
    CLIENT_ID_2 = definition.get("payload").get("client1").get("client_id")


client1 = connect(CLIENT1, CLIENT_ID_1, USER, PASSWORD, SERVER, PORT)
client2 = connect(CLIENT2, CLIENT_ID_2, USER, PASSWORD, SERVER, PORT)


def message(client, userdata, msg):
    vetor = msg.payload.decode().split(",")
    aquecedor("on" if vetor[1] == "1" else "off")
    client1.publish(f"v1/{USER}/things/{CLIENT_ID_1}/response", f"ok,{vetor[0]}")
    client2.publish(f"v1/{USER}/things/{CLIENT_ID_2}/response", f"ok,{vetor[0]}")
    return print(vetor)

#*Subscriber
client1.on_message = message
client1.subscribe(f"v1/{USER}/things/{CLIENT_ID_1}/cmd/2")
client1.loop_start()

# client1.on_message = send_subscribe_response
# client1.subscribe(get_command(USER, CLIENT_ID_1, 2))


client2.on_message = message
client2.subscribe(f"v1/{USER}/things/{CLIENT_ID_2}/cmd/2")
client2.loop_start()


try:
    while True:
        #*Publiser1     
        client1.publish(f"v1/{USER}/things/{CLIENT_ID_1}/data/0", umidade())        
        client1.publish(f"v1/{USER}/things/{CLIENT_ID_1}/data/1", temperatura())

        #*Publiser2
        client2.publish(f"v1/{USER}/things/{CLIENT_ID_2}/data/0", umidade2())
        client2.publish(f"v1/{USER}/things/{CLIENT_ID_2}/data/1", temperatura2())        
        time.sleep(5)

except Exception as e:
    print(e)

client1.loop_stop()
client1.disconnect()
client2.loop_stop()
client2.disconnect()