import random
from random import randint

def criarvetor(t):
    vetor = [0] * t
    for i in range(t):
        numero = random.randint(1, 10)
        vetor[i] = numero
    return vetor

def particao(lista, inicio, fim):
    pivo = lista[inicio]
    i = inicio + 1
    
    for j in range(inicio + 1, fim + 1):
        if lista[j]<pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i = i + 1
    
    lista[inicio], lista[i-1] = lista[i-1], lista[inicio]
    
    return i-1

def bolha(lista, inicio, fim):
    n = fim - inicio + 1
    
    for i in range(n):
        for j in range(inicio, fim-i):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def osdois(lista):
    if len(lista)<=1:
        return lista
    
    k = particao(lista, 0, len(lista)-1)
    
    if k>0:
        bolha(lista, 0, k-1)
    if k<len(lista)-1:
        bolha(lista, k+1, len(lista)-1)
    
    return lista

lista = criarvetor(8)
print(f"Vetor gerado: {lista}")
listafinal = osdois(lista)
print(f"Vetor ordenado: {listafinal}")


#a) Tempo de Execução no melhor caso:
'''O melhor caso ocorre quando a partição é perfeita, ou seja, o pivô divide a lista no meio.
(n/2). Tempo da partição: O(n).
Tempo da bolha no lado esquerdo: O((n/2)^2) = n^2/4
Tempo da bolha no lado direito: O((n/2)^2) = n^2/4
Total do tempo de execução no melhor caso: O(n^2)'''
#b) Tempo de Execução no pior caso:
'''O pior caso ocorre quando a partição é desbalanceada, ou seja, o pivô é menor ou o maior elemento 
Tempo da partição: O(n-1)
Tempo da bolha: (n-1)^2 = O(n^2)
Total do tempo de execução no pior caso: O(n^2)'''