import random
from random import randint




def criarvetor(t):
    vetor = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 100)
        vetor[i] = numero
        
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")

i=0
inv=0
while(i<len(lista)):
    j = i + 1
    
    while j < len(lista):
        if lista[i] > lista[j]:
            inv = inv + 1
        j = j + 1
    i = i + 1   

print(f"Total de inversões: {inv}")