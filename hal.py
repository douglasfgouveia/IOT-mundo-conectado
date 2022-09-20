import random 


def temperatura(temperatura_inicial):
    return temperatura_inicial

def drop_temperatura(valor_inicial):
    valor_inicial +=2
    return valor_inicial      

def raise_temperatura(valor_inicial):
    valor_inicial +=2
    return valor_inicial     

def umidade():
    return  random.randrange(10, 95)

def aquecedor(estado: str):
    if estado == "on":
        return print("Aquecedor Ligado")
    else: 
        return print("Aquecedor Desligado")


