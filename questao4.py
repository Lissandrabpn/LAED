import random
from random import randint


def criarvetor(t):
    vetor = [0] * t
    
    for i in range(t):
        numero = random.randint(1, 7)
        vetor[i] = numero
        
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")

impar = []
i=0
while(i<len(lista)):
    if(lista[i]%2!=0):
        impar.append(lista[i])
    i = i + 1
print(f"Ímpares = {impar}")      

j = 0

while(j<len(impar)):
    atual = impar[j]
    cont = 1
    y = j + 1
    
    while y<len(impar): 
        if(impar[y] == atual):
            cont = cont + 1
        y = y + 1
        
    if cont % 2 != 0:
        print(f"{atual} aparece {cont} vezes")
        break
    j = j + 1       
            
        
    
    
