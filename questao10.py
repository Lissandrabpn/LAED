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
    
def intersecao(p1, p2):
    inicio = Nozin(0)
    fim = inicio
    atual1 = p1
    
    while atual1 is not None: #percorrendo p1
        atual2 = p2 #resetando ponteiro de p2 para q a busca comece do inicio de p2
        encontrou = False
        
        while atual2 is not None: #percorrendo p2
            if atual1.valor == atual2.valor:
                encontrou = True
                break
            atual2 = atual2.proximo
        
        if encontrou: #se o elemento existe em amabs, cria um nó na nova lista 
            fim.proximo = Nozin(atual1.valor)
            fim = fim.proximo
        atual1 = atual1.proximo
    return inicio.proximo

p1 = criarlista([3,9,2,6,4])
p2 = criarlista([4,5,6,2,1])
print("Lista 1:")
imprimir(p1)
print("Lista 2:")
imprimir(p2)
p = intersecao(p1, p2)
print("Lista da interseção: ")
imprimir(p)
            