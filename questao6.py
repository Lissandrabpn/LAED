import random
from random import randint

def criarvetor(t):
    vetor = [0]*t
    
    for i in range(t):
        numero = random.randint(1, 10)
        vetor[i] = numero
    return vetor

lista1 = criarvetor(5)
print(f"Vetor1 gerado: {lista1}")

lista2 = criarvetor(5)
print(f"Veror2 gerado: {lista2}")

for i in lista1:
    cont1 = 0
    cont2 = 0
    
    for elemento in lista1:
        if elemento == i:
            cont1 = cont1 + 1
    
    for elemento in lista2:
        if elemento == i:
            cont2 = cont2 + 1
    
    if cont1 != cont2:
        eh_permutacao = False 
        break

if eh_permutacao:
    print("São permutações!")
else:
    print("Não são permutações.")