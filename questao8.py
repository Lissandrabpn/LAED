class Noduplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

def criarsublista(valores):
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

def imprimir(l):
    for ind, sublista in enumerate(l):
        lista = []
        atual = sublista
        while atual:
            lista.append(str(atual.valor))
            atual = atual.proximo
        print(f"L[{ind}] -> " + " <-> ".join(lista)) 


        
def busca(l, x): #Tempo de execução: O(m + k), onde m é o numero de sublistas e k o tamanho médio de cada sublista
    if not l:
        return None
    
    #encontrar a sublista correta
    sublalvo = None #guardará o ponteiro para a cabeça da sublista onde está o x
    for i in range(len(l)):
        if l[i] is None:
            continue #se sublista na posição i estiver vazia, pula para a aproxima interação
        if i == len(l) -1:
            sublalvo = l[i]
            break #se estivermos na ultima sublista disponivel, assumimos que x so pode estar nela
        
        proxcabeca = l[i+1] #primeiiro nó da proxima sublista
        if proxcabeca is not None and x < proxcabeca.valor:
            #todos os elementos da sublista são menores do que a sublista seguinte 
            sublalvo = l[i]
            break 
    
    if sublalvo is None:
        sublalvo = l[-1]
    
    
    #Busca linear
    atual = sublalvo
    while atual is not None and atual.valor <= x:
        if atual.valor == x:
            return atual
        atual = atual.proximo
    return None


def insercao(l, x): #Tempo de execução: O(m + k)
    novo = Noduplo(x)
    
    if not l:
        l.append(novo)
        return l 
    
    indsublista = len(l) - 1 #definindo o indice da ultima sublista
    for i in range(len(l)-1):
        if l[i+1] is not None and x < l[i+1].valor:
            indsublista = i
            break
    #percorre o veotr l para identificar em qual intervalo x se encaixa
    
    cabeca = l[indsublista]
    if cabeca is None:
        l[indsublista] = novo
        return l
    
    #inserção no inicio da sublista
    if x < cabeca.valor:
        novo.proximo = cabeca
        cabeca.anterior = novo
        l[indsublista] = novo
        return l
    
    #insreção no meio ou no fim da sublista
    atual = cabeca
    while atual.proximo is not None and atual.proximo.valor < x:
        atual = atual.proximo 
    
    novo.proximo = atual.proximo
    novo.anterior = atual
    
    if atual.proximo is not None: 
        atual.proximo.anterior = novo
    
    atual.proximo = novo
    
    return l 

def remocao(l, x): #Tempo de execução: O(m + k)
    
    if not l:
        return l
    
    #localiza a sublista
    indsublista = -1
    for i in range(len(l)):
        if l[i] is None:
            continue
        if i == len(l) - 1:
            indsublista = i
            break
        if l[i+1] is not None and x < l[i+1].valor:
            indsublista = i
            break
        
        
    if indsublista == -1:
        return l
    atual = l[indsublista]
    
    #procura o nó com o valor x
    while atual is not None and atual.valor < x:
        atual = atual.proximo
    
    if atual is None or atual.valor != x:
        return l
    
    #remoção do nó ajustando os ponteiros
    if atual.anterior is not None:
        atual.anterior.proximo = atual.proximo
    else:
        l[indsublista] = atual.proximo
    
    if atual.proximo is not None:
        atual.proximo.anterior = atual.anterior
    
    return l

l = [
    criarsublista([2, 9]),
    criarsublista([15, 19])
]
    
imprimir(l)
no = busca(l, 19)
print(f"Busca por 19: {'encontrado' if no else 'não encontrado'}")

print("Inserindo o 17:")
insercao(l, 17)
imprimir(l)

print("Removendo o 9")
remocao(l, 9)
imprimir(l)