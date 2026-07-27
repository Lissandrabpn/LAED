import random
from random import randint




def criarvetor(t):
    vetor = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 100)
        vetor[i] = numero
        
    return vetor

lista = criarvetor(10)
print(f"Vetor gerado: {lista}")

#algoritmo da bolha
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if(lista[j]>lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

print("Vetor ordenado:", lista)


terceiro = lista[len(lista)-3]


print(f"Terceiro maior={terceiro}")