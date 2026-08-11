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

def trocarnos(a, b, cabeca):
    #"a" vem antes de "b"
    anta = a.anterior
    proxb = b.proximo
   
   #ajustando o nó que vem antes de "a" 
    if anta is not None: #proximo do anterior de "a" aponta para o "b" (nó novo)
        anta.proximo = b
    else: #"a" era a cabeça da lista 
        cabeca = b
    
    #ajustando o nó que vem depois de "b"
    if proxb is not None:
        proxb.anterior = a #proximo do anterior de "b" aponta para "a"
    
    b.anterior = anta
    b.proximo = a
    
    a.anterior = b
    a.proximo = proxb
    
    return cabeca 

def varredura(p):
    if p is None or p.proximo is None: #lista vazia ou tem só um nó
        return p
    
    q = p
    
    while q is not None and q.proximo is not None:
        if q.valor>q.proximo.valor:
            p = trocarnos(q, q.proximo, p)
        else:
            q = q.proximo
    return p

p = criarlistadupla([1, 3, 4, 5, 9, 7, 8])
print("Lista original:")
imprimir(p)
var = varredura(p)
print("Lista após uma varredura:")
imprimir(var)
#Tempo de execução: O(n) para apenas uma varredura