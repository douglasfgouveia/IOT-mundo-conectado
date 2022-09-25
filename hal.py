import time
import random 

def temperatura(temperatura_inicial):
    return temperatura_inicial

def drop_temperatura(valor):
    valor -= 2   
    return valor

def raise_temperatura(valor):
    valor +=2
    return valor     

def umidade(umidade_inicial):
   return umidade_inicial

def aquecedor(estado: str):
    temp = 0
    while True:
        if estado == "on":
            temp_inicial = temperatura(raise_temperatura(temp))
            temp_final = temp + temp_inicial
            return print(f"temperatura atual subiu {temp_final}")
        else: 
            temp_inicial = temperatura(drop_temperatura(temp))
            temp_final = temp + temp_inicial
            return print(f"temperatura atual caiu {temp_final}")
            # return print("Aquecedor Desligado")
