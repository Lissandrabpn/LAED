class Nozin: #criando uma classe nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None #n aponta para ninguem

def movermaior(p):
    if p is None or p.proximo is None: #se a lista estiver vazia ou apenas um elemento
        return p
    maior = p
    anteriormaior = None
    atual = p
    anterioratual = None
    
    while atual is not None:
        if atual.valor > maior.valor: #se o atual for maior que o maior, atualiza o maior e seu anterior
            maior = atual
            anteriormaior = anterioratual
        anterioratual = atual #dando um passo para frente
        atual = atual.proximo
    
    if maior.proximo is None:
        return p #se o maior já for o ultimo
    
    ultimo = p
    
    while ultimo.proximo is not None:
        ultimo = ultimo.proximo #percorrendo a lista até cehgar no ultimo nó
    
    #desconecatndo o maior nó de onde ele estava
    if anteriormaior is None: #maior era a cabeça
        p = maior.proximo
    else:#nó no meio da lista
        anteriormaior.proximo = maior.proximo
    
    #colocando o maior nó no final
    ultimo.proximo = maior
    maior.proximo = None
    
    return p

def imprimirlista(p):
    lista = []
    atual = p
    
    while atual is not None:
        lista.append(str(atual.valor))
        #str = converte o numero para string
        atual = atual.proximo 
    
    print("->".join(lista)+"-> None")
    #.join() serve para juntar varios elementos usando um separador, esse método exige que todos os elementos da lista sejam string


def criarlista(valores):
    if not valores: #se a lista for vazia, retorna none
        return None
    cabeca = Nozin(valores[0]) #primeiro nó da lists
    atual = cabeca
    for i in valores[1:]: #percorre o restante da lista apartir do segundo elemento
        atual.proximo = Nozin(i)
        atual = atual.proximo
    return cabeca

#Tempo de execução = O(n)
#testando
p = criarlista([1, 3, 14, 9, 4])
print("Lista original:")
imprimirlista(p)
p = movermaior(p)
print("Lista alterada:")
imprimirlista(p)