import random 
from random import randint

def criarvetor(t):
    vetor = [0]*t
    
    for i in range(t):
        numero = random.randint(1, 10)
        vetor[i] = numero
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")



for k in lista: 
    
    menorum = False
    maiorum = False
    
    for elemento in lista:
        if elemento == k-1:
            menorum = True
        if elemento == k+1:
            maiorum = True
    
    if not menorum and not maiorum:
        print(f"Sim, o {k}")

