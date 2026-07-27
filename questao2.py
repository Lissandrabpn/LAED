#primeira questão
'''import random
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
    print(f"Não há impares no vetor") '''

#segunda questão 
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



if len(impar)>= 2:
    if (impar[0]>impar[1]):
        maior1 = impar[0]
        maior2 = impar[1]
    else:
        maior1 = impar[1]
        maior2 = impar[0]
    
    j = 2
    while(j<len(impar)):
        if(impar[j]>maior1):
            maior2 = maior1
            maior1 = impar[j]
        elif(impar[j] > maior2 and impar[j] != maior1):
            maior2 = impar[j]
        
        j = j + 1
        
    print(f"Maior número ímpar: {maior1}")
    print(f"Segundo maior número ímpar: {maior2}")
    
elif len(impar) == 1:
    print(f"Só há um número ímpar no vetor ({impar[0]}), não existe segundo maior.")
else:
    print("Não há ímpares no vetor.")
    




 