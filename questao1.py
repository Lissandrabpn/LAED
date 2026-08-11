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
        novo = Noduplo(i) #cria um nó de valor i
        atual.proximo = novo #proximo atual aponta para novo
        novo.anterior = atual #anterior do novo aponta para atual
        atual = novo #avança o ponteiro atual
    return cabeca

def imprimirdupla(p):
    lista = []
    atual = p
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("None <-> " + " <-> ".join(lista) + " <-> None")

def elementocentral(p):
    if p is None:
        return None
    
    lento = p #vai anadar de 1 em 1 nó
    rapido = p #vai andar de 2 em 2 nó
    
    while rapido.proximo is not None and rapido.proximo.proximo is not None:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
    return lento.valor #posicionado no meio da lista
#como o rapido avança o dobro do lento, quando o rapido chegra no final, o lento estara no meio da lista

p = criarlistadupla([3, 9, 5, 2, 8, 10])
central = elementocentral(p)
print(f"Elemento central:  {central}")

#Tempo de execução: O(n)