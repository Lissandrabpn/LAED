class Noesparso:
    def __init__(self, valor, indice):
        self.valor = valor
        self.indice = indice
        self.proximo = None
        self.anterior = None

def buscaindice(p, k): #Tempo de execução: O(k), onde k é o numero de elementos guardados na lista
    atual = p
    #percorre a lista enquanto o indice do nó for menor que k
    while atual is not None and atual.indice < k:
        atual = atual.proximo
    
    #se encontra atual.indice==k retorna atual.valor
    if atual is not None and atual.indice == k:
        return atual.valor 
    
    return 0 #se o indice não esta na lista

def buscavalor(p, x): #Tempo de execução: O(k)
    atual = p
    while atual is not None:
        if atual.valor == x:
            return atual.indice
        atual = atual.proximo
    return -1 #valor não encontrado

def atualizacao(p, x, k): #Tempo de execução: O(k)
    atual = p
    anterior = None
    
    while atual is not None and atual.indice < k:
        anterior = atual
        atual = atual.proximo
     
     #k esta na lista   
    if atual is not None and atual.indice == k:
        if x != 0: #x diferente de zero
            atual.valor = x
        else: #x == 0, tem q remover o x
            if atual.anterior is not None: #se o nó não for o primeiro da lista
                atual.anterior.proximo = atual.proximo
            else: #se for o primeiro nó da lista
                p = atual.proximo
            if atual.proximo is not None:
                atual.proximo.anterior = atual.anterior
    
    # k não esta na lista e x é diferente de zero
    elif x != 0:
        novo = Noesparso(x, k) #criando um novo nó de valor x e indice k
        
        if anterior is None: #se a inserção for no inicio da lista
            novo.proximo = p
            if p is not None:
                p.anterior = novo
            p = novo
        
        else: #inserção no meio ou no final da lista 
            novo.proximo = atual #engatando o novo nó entre anterior e atual
            novo.anterior = anterior 
            anterior.proximo = novo
            if atual is not None:
                atual.anterior = novo
    return p

def vetoresparso(V):
    i = Noesparso(0, 0)
    f = i
    
    for pos, v in enumerate(V, start = 1):
        if v != 0:
            novo = Noesparso(v, pos)
            
            f.proximo = novo
            novo.anterior = f
            f = novo
    cabeca = i.proximo
    if cabeca is not None:
        cabeca.anterior = None
    return cabeca

def imprimiresparso(p):
    lista = []
    atual = p
    while atual:
        lista.append(f"[{atual.valor} | {atual.indice}]")
        atual = atual.proximo
    print("None <-> " + " <-> ".join(lista) + " <-> None")

V = [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]
p = vetoresparso(V)

#a1) Busca por indice: 
print("Busca pelo indice 8:")
busca1 = buscaindice(p, 8)
print(f"Valor: {busca1}")

#a2) Busca por valor:
print("Busca pelo valor 7:")
busca2 = buscavalor(p, 7)
print(f"Posição: {busca2}")

#a3) Atualização 
print("Vetor antes da atualização:")
imprimiresparso(p)
p = atualizacao(p, 9, 10)
print("Vetor após a atualiazação:")
imprimiresparso(p)

