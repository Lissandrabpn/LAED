import random
from random import randint

def criarvetor(t):
    vetor = [0] * t
    for i in range(t):
        numero = random.randint(1, 10)
        vetor[i] = numero
    return vetor

def bolha(lista, inicio, fim):
    n = fim - inicio + 1
    for i in range(n):
        for j in range(inicio, fim-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def ostres(lista):
    n = len(lista)
    if n <= 1:
        return lista
    
    doisterco = (2*n)//3
    if doisterco>1:
        bolha(lista, 0, doisterco-1)
        print(f"Primeiros 2n/3 ordenados: {lista}")
    
    ultimo = n - doisterco
    if doisterco>1:
        bolha(lista, ultimo, n-1)
        print(f"Últimos 2n/3 ordenados: {lista}")
    
    if doisterco>1:
        bolha(lista, 0, doisterco-1)
        print(f"Os primeiros 2n/3 ordenados de novo: {lista}")
    
    return lista

lista = criarvetor(9)
print(f"Vetor gerado = {lista}")
listafinal = ostres(lista)
print(f"Vetor ordenado: {listafinal}")

#a) Ao final do processo a lista está completamente ordenada? Porque?
'''Sim, está toda ordenada. Pois divide a lista em três partes iguais de tamanho n/3,
a parte inicial, a do meio e a final. Primeiro ordena os 2n/3, estamos ordenando as duas primeiras partes.
Após ordenar as duas primeiras partes os maiores elementos de toda a lista são jogados para a terça parte final.
Como a terça parte final já está com os maiores elementos, basta ordenar novamente as duas primeiras partes.'''
#b)Analise o tempo de execução desse procedimento: 
'''A bolha é chamada três vezes. O((2n/3)^2) = O(n^2)
Tempo total: 3 * O(n^2) = O(n^2)'''