class Noesparso:
    def __init__(self, valor, indice):
        self.valor = valor
        self.indice = indice
        self.proximo = None
        self.anterior = None

def vetoresparso(V):
    i = Noesparso(0, 0) #inicio
    f = i #fim
    
    for pos, v in enumerate(V, start=1): #pos é o indice atual e v é o numero contido no vetor
        if v != 0:#checando se o elemento atual é diferente de zero
            novo = Noesparso(v, pos) #cria um novo nó onde guarda seu valor e seu indice 
            
            f.proximo = novo #conectando o novo nó ao fim da lista
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
print("Vetor esparso original:")
print(V)
p = vetoresparso(V)
print("Vetor esparso na lista duplamente enecadeada:")
imprimiresparso(p)

#Tempo de execução: O(n)