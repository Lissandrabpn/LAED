import random
from random import randint

def criarmatriz(n):
    
    matriz = [0] * n
    for i in range(n):
        linha = [0] * n
        for j in range(n):
            
            numero = random.randint(1, 5)
            linha[j] = numero
        matriz[i] = linha
    return matriz

def linhasiguais(matriz):
    n = len(matriz)
    
    
    for i in range(n):
        for j in range(i + 1, n):
            
            if matriz[i] == matriz[j]:
                print(f"=> Sim, as linhas {i+1} e {j+1} são exatamente iguais.")
                return True
                
    print("=> Não existem linhas exatamente iguais na matriz.")
    return False

mmatriz = criarmatriz(4)
    
print("Matriz M Gerada:")
for linha in mmatriz:
        print(linha)
    
linhasiguais(mmatriz)