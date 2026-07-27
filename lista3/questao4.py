import random
from random import randint

def criarmatriz(n):
    
    matriz = [0] * n
    for i in range(n):
    
        linha = [0] * n
        for j in range(n):
            numero = random.randint(1, 20)
            linha[j] = numero
        
        matriz[i] = linha
    return matriz

def verificarrepetidos(matriz):
    
    n = len(matriz)
    elementosvistos = set() #não permite elementos duplicados
    
    
    for i in range(n):
        for j in range(n):
            elementoatual = matriz[i][j]
            
            
            if elementoatual in elementosvistos:
                print(f"=> Sim, o elemento {elementoatual} aparece mais de uma vez.")
                return True
                
        
            elementosvistos.add(elementoatual)
            
    print("=> Não existem elementos repetidos na matriz.")
    return False

mmatriz = criarmatriz(6)
print("Matriz gerada:")
for linha in mmatriz:
    print(linha)
verificarrepetidos(mmatriz)