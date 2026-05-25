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

k = int(input("Digite um número: "))

i=0
achou = False
menordif = 999

while(i<len(lista)):
    if(lista[i]==k):
        print(f"Achei {k}")
        achou = True
        break
    
    dif = abs(k - lista[i]) #valor absoluto, positivos 
        
    if(dif < menordif):
            menordif = dif
            prox = lista[i]
    i = i + 1

if not achou:
    print(f"{k} não está, valor próximo: {prox}")     
                   