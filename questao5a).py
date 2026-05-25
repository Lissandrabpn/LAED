import random
from random import randint




def criarvetor(t):
    vetor = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 20)
        vetor[i] = numero
        
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")

i = 0
j = i + 1
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] == 2 * lista[j] or lista[j] == 2 * lista[i]:
            print(f"Achei {lista[i]} e {lista[j]}")
            break
    