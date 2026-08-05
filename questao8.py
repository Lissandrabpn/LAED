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

def elemfrequencia(p):
    if p is None:
        return None, 0 #retorna None e zero para ocorrencias
    frequencia = {}
    #criando um dicionário(tabela hash), onde armazena os pares {valordono: ocorrencias}
    atual = p
    
    while atual is not None:
        valor = atual.valor #guardando o valor de cada nó
        if valor in frequencia: #se o valor ja foi visto antes, incrementa a contagem
            frequencia[valor] = frequencia[valor] + 1
        else: #se é a primeira vez q foi visto, apenas adiciona a primeira ocorrencia
            frequencia[valor] = 1
    #quando o laço while encerra o dicionário estará totalmente preenchido 
        atual = atual.proximo
    maisfreq = None
    maxocor = 0
    
    for valor, contagem in frequencia.items():
    #criando um laço for que itera por cada par (valor, contagem) registrado dentro do dicionário frequencias
        if contagem > maxocor:
            maxocor = contagem
            maisfreq = valor
    return maisfreq, maxocor

p = criarlista([8, 3, 8, 5, 8, 3])
print("Lista original:")
imprimir(p)
p = elemfrequencia(p)
print("(valor do nó com mais ocorrencias, ocorrencias):")
print(p)
               
#Tempo de execução: O(n)