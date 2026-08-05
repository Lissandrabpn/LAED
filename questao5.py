class Nozin:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    

def intercalar(p1, p2):
    outrono = Nozin(0) #nó auxiliar para servir de ponto inicial
    atual = outrono
    
    while p1 is not None and p2 is not None:
        if p1.valor <= p2.valor:
            atual.proximo = p1
            p1 = p1.proximo
        else:
            atual.proximo = p2
            p2 = p2.proximo
        
        atual = atual.proximo
    
    if p1 is not None: #se sobrou algum elemento
        atual.proximo = p1
    elif p2 is not None:
        atual.proximo = p2
    
    return outrono.proximo

def imprimir(p):
    lista = []
    atual = p
    
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("->".join(lista)+"-> None")

def criarlista(valores):
    if not valores:
        return None
    cabeca = Nozin(valores[0])
    atual = cabeca
    for i in valores[1:]:
        atual.proximo = Nozin(i)
        atual = atual.proximo
    return cabeca


p1 = criarlista([3, 6, 7, 10, 15])
p2 = criarlista([2, 4, 9, 11, 14])
print("Lista p1:")
imprimir(p1)
print("Lista p2:")
imprimir(p2)
p = intercalar(p1, p2)
print("Lista intercalada:")
imprimir(p)     

#Tempo de execução: O(n + m), onde n é o tamanho de p1 e m o tamanho de p2