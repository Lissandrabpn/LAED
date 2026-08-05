class Nozin:
    def __init__(self,valor):
        self.valor = valor
        self.proximo = None

def duplicarimpar(p):
    atual = p
    while atual is not None:
        if atual.valor % 2 != 0: #se for impar
            novono = Nozin(atual.valor)#criando um novo nó com o mesmo valor
            novono.proximo = atual.proximo
            atual.proximo = novono
            atual = novono.proximo
        else: #se for par apenas avança
            atual = atual.proximo
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

p = criarlista([1,4,2,3,5,9])
print("Lista original:")
imprimirlista(p)
p = duplicarimpar(p)
print("Lista alterada:")
imprimirlista(p)
#Tempo de execução: O(n)