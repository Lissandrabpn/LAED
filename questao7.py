class Noduplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

def transflistadelistas(p, k): #k é o tamanho das sublistas
    if p is None or k <= 0:
        return []
    
    l = []
    atual = p
    
    while atual is not None:
        l.append(atual) #guarda a cabeca da sublista atual
        cont = 1
        
        while atual.proximo is not None and cont < k:
            atual = atual.proximo #avançando o ponteiro até o ultimo elemento da sublista
            cont += 1
        
        proxsublista = atual.proximo #salvando o inicio da proxima sublista
        
        atual.proximo = None #desconecta a sublista atual da proxima
        if proxsublista is not None:
            proxsublista.anterior = None #corta a conexão para trás

        atual = proxsublista #avança para o inicio da proxima sublista
    return l


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

def imprimirlistadelistas(l):
    for ind, sublista in enumerate(l): #ind = indice da sublista dentro do vetor l
        lista = []
        atual = sublista
        while atual:
            lista.append(str(atual.valor))
            atual = atual.proximo
        print(f"L[{ind}] -> None <-> " + " <-> ".join(lista) + " <-> None")

p = criarlistadupla([1, 3, 7, 10, 13, 18, 21, 27, 49, 53])
print("Transformando a lista em sublista de tamanho k=4:")
l = transflistadelistas(p, 4)
imprimirlistadelistas(l)