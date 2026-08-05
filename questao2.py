class Nozin: #criando uma classe nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None #n aponta para ninguem

def separar(p):
    #ponteiros de inicio e fim para impares
    i1 = None 
    f1= None
    #ponteiros para inicio e fim para pares
    i2 = None
    f2 = None
    
    atual = p
    while atual is not None:
        #guardando o proximo 
        proximono = atual.proximo
        atual.proximo = None
        
        if atual.valor % 2 != 0: #se for impar
            if i1 is None:
                i1 = atual
                f1 = atual
            else:
                f1.proximo = atual
                f1 = atual
        
        else: #se for par
            if i2 is None:
                i2 = atual
                f2 = atual
            else: 
                f2.proximo = atual
                f2 = atual
        
        atual = proximono
    return i1, i2

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
#Testando
p = criarlista([1,4,7,10,3,5,14,45,2])
print("Lista original:")
imprimirlista(p)
p1, p2 = separar(p)
print("Lista impares:")
imprimirlista(p1)
print("Lista pares:")
imprimirlista(p2)