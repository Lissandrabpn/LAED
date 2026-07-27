import random
from random import randint


def criarvetor1(t):
    vetor1 = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 10)
        vetor1[i] = numero
        
    return vetor1

lista1 = criarvetor1(5)
print(f"Vetor1 gerado: {lista1}")


import random
from random import randint


def criarvetor2(t):
    vetor2 = [0] * t
    
    for j in range(t):
        numero2 = random.randint(1, 10)
        vetor2[j] = numero2
        
    return vetor2

lista2 = criarvetor2(5)
print(f"Vetor2 gerado: {lista2}")

achei = []
for i in range(len(lista1)):
    for j in range(len(lista2)):
        if(lista1[i]==lista2[j]):
            achei.append(lista1[i])
    j=j+1
i=i+1

print(achei)