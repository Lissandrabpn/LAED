class Nozin:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
def criarlista(valores):
    if not valores:
        return None

    cabeca = Nozin(valores[0])
    atual = cabeca
    for i in valores[1:]:
        atual.proximo = Nozin(i)
        atual = atual.proximo 
    return cabeca

def imprimir(p):
    lista = []
    atual = p
    while atual is not None:
        lista.append(str(atual.valor))
        atual = atual.proximo
    print("->".join(lista)+"-> None")
    
def repetido(p):
    atual = p
    while atual is not None:
        chec = p
        while chec != atual:
            if chec.valor == atual.valor:
                return True
            chec = chec.proximo
        atual = atual.proximo
    return False

p = criarlista([2,4,5,6,7,8,9])
print("Lista:")
imprimir(p)
resposta = "Sim" if repetido(p) else "Não"
print(resposta)  
#Tempo de execução: O(n^2)