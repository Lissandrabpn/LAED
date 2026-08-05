class Nozin:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
def criarlista(valores):
    if not valores:
        return None
    cabeca = Nozin(valores[0])
    atual = cabeca
    for i in valores[1:]:
        atual.proximo = Nozin(i)
        atual = atual.proximo
    return cabeca

def imprimir(p):
    lista = []
    atual = p
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("->".join(lista)+"-> None")

def removercopia(p, k):
    inicio = Nozin(0)
    inicio.proximo = p
    
    anterior = inicio
    atual = p
    
    while atual is not None:
        if atual.valor == k:
            anterior.proximo = atual.proximo
            #nó anterior pula o nó atual e faz o seu proximo apontar pra proximo do atual
        else:
            anterior = atual
            #se o nó atual não deve ser removido, anterior da um passo à frente e passa a ser o nó atual
        atual = atual.proximo 
    
    return inicio.proximo 

p = criarlista([1, 3, 3, 2, 3, 2])
print("Lista original:")
imprimir(p)
p = removercopia(p, 3)
imprimir(p)
#Tempo de execução: O(n)
            
        


        