import random
from random import randint




def criarvetor(t):
    vetor = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 10)
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

print("Vetor ordenado:", lista)

i=0
j=0
while(i<len(lista) and j<len(lista)):
    if i!=j and lista[j] == 2*lista[i]:
        print(f"Sim, {lista[i]} e {lista[j]}")
        break
    elif lista[j] < 2*lista[1]:
        j = j + 1
    else:
        i = i + 1
    if i == j:
        j = j + 1
print("Nãó")
        