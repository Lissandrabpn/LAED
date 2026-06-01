import random
from random import randint

def criarvetor(t):
    vetor = [0]*t
    
    for i in range(t):
        numero = random.randint(1, 100)
        vetor[i] = numero
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")

#algoritmo da bolha
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if(lista[j]>lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

print(f"Vetor ordenado: {lista}")

k = int(input("Digite um número: "))

kesimo = lista[len(lista)-k]

print(f"{k} maior elemento: {kesimo}")