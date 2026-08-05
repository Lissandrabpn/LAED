class Nozin:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def particao(p, k):
    atual = p
    #ponteiros para o inicio da sublistas
    imenores = Nozin(0)
    imaiores = Nozin(0)
    #ponteiros para o final das sublistas
    fmenores = imenores
    fmaiores = imaiores
    
    while atual is not None:
        proximono = atual.proximo #guardando o proximo no do atual
        atual.proximo = None 
        if atual.valor <= k:
            fmenores.proximo = atual
            fmenores = atual
        else:
            fmaiores.proximo = atual
            fmaiores = atual
        atual = proximono
    fmenores.proximo = imaiores.proximo
    return imenores.proximo

def imprimir(p):
    lista = []
    atual = p
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("->".join(lista)+"-> None")

def criarlista(valores):
    if not valores:
        return None
    cabeca = Nozin(valores[0]) 
    atual = cabeca
    for i in valores[1:]:
        atual.proximo = Nozin(i)
        atual = atual.proximo
    return cabeca

p = criarlista([1, 4, 8, 10, 6, 20])
print("Lista:")
imprimir(p)
p = particao(p, 6)
print("Partição:")
imprimir(p)

#Tempo de execução: O(n)