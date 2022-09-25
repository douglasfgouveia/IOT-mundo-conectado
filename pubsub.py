import paho.mqtt.client as mqtt

def connect(client, client_id, user, password, server, port):
    client = mqtt.Client(client_id)
    client.username_pw_set(user, password)
    client.connect(server, port)
    return client

def send_subscribe_response(client,user, client_id, vetor_payload):
    client.publish(f"v1/{user}/things/{client_id}/response", f"ok,{get_vetor_payload}")
    return client

def get_vetor_payload(client, userdata, msg):
    vetor_payload = msg.payload.decode().split(",")
    return vetor_payload

def get_command(user,client_id, device_channel):
    return f"v1/{user}/things/{client_id}/cmd/{device_channel}"