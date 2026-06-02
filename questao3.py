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

lista1 = criarvetor(8)
lista2 = criarvetor(8)
print(f"Vetor 1 gerado: {lista1}")
print(f"Vetor 2 gerado: {lista2}")

bolha(lista1, 0, len(lista1)-1)
bolha(lista2, 0, len(lista2)-1)
print(f"Vetor 1 ordenado: {lista1}")
print(f"Vetor 2 ordenado: {lista2}")

def encontrarmediana(A, B):
    
    n = len(A)
    inicio = 0
    fim = n
    
    while inicio <= fim:
        i = (inicio + fim) // 2  #lista A
        j = n - i               #listaB 
        
        #lista A
        if i > 0:
            Aesquerda = A[i-1]
        else:
            Aesquerda = float('-inf')
            
        if i < n:
            Adireita = A[i]
        else:
            Adireita = float('inf')
            
        #lista B
        if j > 0:
            Besquerda = B[j-1]
        else:
            Besquerda = float('-inf')
            
        if j < n:
            Bdireita = B[j]
        else:
            Bdireita = float('inf')
            
        
        if Aesquerda <= Bdireita and Besquerda <= Adireita:
            # Pega o maior elemento do lado esquerdo
            if Aesquerda > Besquerda:
                maxesquerda = Aesquerda
            else:
                maxesquerda = Besquerda
                
            
            if Adireita < Bdireita:
                mindireita = Adireita
            else:
                mindireita = Bdireita
                
    
            return (maxesquerda + mindireita) / 2
            
        elif Aesquerda > Bdireita:
            fim = i - 1  
        else:
            inicio = i + 1

resultadomed = encontrarmediana(lista1, lista2)
print(f"Mediana: {resultadomed}")