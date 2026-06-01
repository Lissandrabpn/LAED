import random 
from random import randint

def criarvetor(t):
    vetor = [0]*t
    
    for i in range(t):
        numero = random.randint(1, 10)
        vetor[i] = numero
    return vetor

lista = criarvetor(5)
print(f"Vetor gerado: {lista}")

n = int(input("Digite um número: "))
k = int(input("Digite a quantidade mínima de repetições: "))

cont = 0

for elemento in lista:
    if elemento == n:
        cont = cont + 1

if cont>=k:
    print(f"Sim, {n} aparece {cont} vezes")
else:
    print(f"Não, {n} aparece apenas {cont} vezes")
    