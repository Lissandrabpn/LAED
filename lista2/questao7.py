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

k = int(input("Digite um número: "))

achou = False
for i in range(len(lista)):
    atual = lista[i]
    
    for j in range(i+1, min(i+1+k, len(lista))):
        frente = lista[j]
        
        if(atual == frente):
            print("Achei")
            d = j-i
            print(f"A distância entre eles: {d} - máximo: {k}")
            achou = True
            break
    if achou:
        break
if not achou:
    print(f"Nenhum repetido encontrado na distância de até {k}")