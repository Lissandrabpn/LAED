class Noduplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None 
        
def criarlista(valores):
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

def particiona(p, k):
    if p is None:
        return p
    
    q = p #q aponta para o primeiro nó
    r = p #r aponta para o último nó
    
    while r.proximo is not None:
        r = r.proximo #posicionando o ponteiro r no final da lista 
    
    while q is not None and r is not None and q != r and q.anterior != r:
    #o laço para quando q e r forem nulos, quando os ponteiros se encontrarem e quando se cruzarem(q passou pra direita de r)
        while q is not None and q != r and q.valor<=k:
           q = q.proximo #q avança da esquerda para a direita
        
        while r is not None and q != r and r.valor>k:
            r = r.anterior #r avança da direita para esquerda 
        
        if ( q is not None
            and r is not None
            and q != r
            and q.anterior != r
            and q.valor > k
            and r.valor <= k):
            q.valor, r.valor = r.valor, q.valor
            q = q.proximo
            r = r.anterior
    return p
    


p = criarlista([1, 9, 4, 2, 10])
print("Lista original:")
imprimir(p)
part = particiona(p, 4)
print("Lista após a partição sendo k = 4:")
imprimir(part)

#Tempo de execução: O(n)