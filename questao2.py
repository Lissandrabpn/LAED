class Noduplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

def criarlistadupla(valores):
    if not valores:
        return None
    cabeca = Noduplo(valores[0])
    atual = cabeca
    for i in valores[1:]:
        novo = Noduplo(i)
        atual.proximo = novo
        novo.anterior = atual
        atual = novo
    return cabeca 

def imprimir(p):
    lista = []
    atual = p
    
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("None <-> " + " <-> ".join(lista) + " <-> None")

def atualizar(p, x, y):
    atual = p
    
    #laço para assim que encontrar um nó seja igual a x ou quando chegar ao fim da lista
    while atual is not None and atual.valor != x:
        atual = atual.proximo
    
    if atual is None: #se n encontrou x 
        return p #retorna a lista
    
    atual.valor = y #modificando o valor para y
    
    #se y ficou maior que o proximo, move para a direita
    while atual.proximo is not None and atual.valor > atual.proximo.valor:
    #enquanto existir o nó seguinte e o valor do nó atual for maior que o valor do nó seguinte
        atual.valor, atual.proximo.valor = atual.proximo.valor, atual.valor
        #troca entre o atual e o seu proximo
    
    #se y ficou menor que o anterior, move para a esquerda
    while atual.anterior is not None and atual.valor < atual.anterior.valor:
        atual.valor, atual.anterior.valor = atual.anterior.valor, atual.valor
        atual = atual.anterior
    
    return p

p = criarlistadupla([3, 5, 9, 10, 15])
print("Lista original:")
imprimir(p)
p = atualizar(p, 9, 12)
print("Atualizando o 9 para o 12")

#Tempo de execução: O(n)
        