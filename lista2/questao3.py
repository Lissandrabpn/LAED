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

soma = 0
for i in range(len(lista)):
    soma = soma + lista[i]

media = soma/len(lista)

print(f"Média: {media}")

prox = lista[0]
menordif = abs(lista[0] - media)

for elemento in lista[1:]:
    difatual = abs(elemento - media)
    
    if difatual<menordif:
        menordif = difatual
        prox = elemento
    
print(f"Elemento mais próximo da média: {prox}")


