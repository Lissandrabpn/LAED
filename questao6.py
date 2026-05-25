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

#algoritmo da bolha
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if(lista[j]>lista[j+1]):
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

print("Vetor ordenado:", lista)

i=0
menordif = 999

while i<len(lista)-1:
    dif = abs(lista[i]-lista[i+1])
    
    if(dif<menordif):
        menordif = dif
        num1 = lista[i]
        num2 = lista[i+1]
    
    i = i + 1

print(f"Os números mais próximos são {num1} e {num2}")