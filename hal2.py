
import paho.mqtt.client as mqtt
import random


def controleTemperatura(x):
    globals()['cont'] = x
    return cont

def aquecedor(estado: str):
    if estado == "on":
        print("relé LIGADO")
        globals()['bot'] = 1
    else:
        print("relé DESLIGADO")
        globals()['bot'] = 0
    return estado

def temperatura():
    if bot == 1:
        if globals()['temp'] < cont:
            globals()['temp'] -= 1
        if globals()['temp'] > cont:
            globals()['temp'] += 1
    elif bot == 0:
        if globals()['temp'] > 10:
            globals()['temp'] -= 1
    return temp

def umidade():
    if bot == 1:
        if globals()['umid'] > 60:
            globals()['umid'] -= 1        
    elif bot == 0:
        if globals()['umid'] < 99:
            globals()['umid'] += 1
    return umid

def temperatura2():
    if bot == 1:
        if globals()['temp2'] < cont:
            globals()['temp2'] += 1
        if globals()['temp2'] > cont:
            globals()['temp2'] -= 1
    elif bot == 0:
        if globals()['temp2'] > 15:
            globals()['temp2'] -= 1
    return temp2

def umidade2():
    if bot == 1:
        if globals()['umid2'] > 60:
            globals()['umid2'] -= 1
    elif bot == 0:
        if globals()['umid2'] < 99:
            globals()['umid2'] += 1
    return umid2

cont = 0
bot = 0

temp = 10
umid = 60
temp2 = 20
umid2 = 70
