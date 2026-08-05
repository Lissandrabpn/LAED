class Nozin: #criando uma classe nó
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None #n aponta para ninguem


def inverter(p):
    anterior = None
    atual = p
    
    while atual is not None:
        proximono = atual.proximo
        atual.proximo = anterior #inverte o ponteiro do atual para apontar para o anterior
        #avançando os ponteiros
        anterior = atual
        atual = proximono
    return anterior #nova cabeça da lista

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


p = criarlista([1,3,4,7,9])
print("Lista original:")
imprimirlista(p)
p = inverter(p)
print("Lista invertida:")
imprimirlista(p)