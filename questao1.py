
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

impar = []
i=0

while(i<len(lista)):
    if(lista[i] % 2 != 0):
        impar.append(lista[i])
    i = i+1


maior = impar[0]
if len(impar)>0:
    j=1
    maior = impar[0]
    
    while(j<len(impar)):
        if(impar[j]>maior):
            maior = impar[j]
        j = j+1
    

    print(f"Maior número ímpar: {maior}")     
else:
    print(f"Não há impares no vetor") 

