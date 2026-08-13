class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
    
    def push(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        return removido.dado

    def is_empty(self):
        return self.topo is None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novo_no = No(valor)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def dequeue(self):
        if self.inicio is None:
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return removido.dado

    def is_empty(self):
        return self.inicio is None
    

def inverterfila(fila : Fila) -> None:

    pilha_auxiliar = Pilha()
    
    # 1. Esvazia a fila enfileirando os elementos na pilha
    while not fila.is_empty():
        pilha_auxiliar.push(fila.dequeue())
        
    # 2. Desempilha os elementos e insere de volta na fila
    while not pilha_auxiliar.is_empty():
        fila.enqueue(pilha_auxiliar.pop())
    
    
''' (a) Traçando a execução para a fila <1, 2, 3, 4> 

# Primeira etapa (fila -> pilha):
  Dequeue() = 1, Push(1) -> pilha: topo -> 1 -> 
  Dequeue() = 2, Push(2) -> pilha: topo -> 2 -> 1 -> 
  Dequeue() = 3, Push(3) -> pilha: topo -> 3 -> 2 -> 1 -> 
  Dequeue() = 4, Push(4) -> pilha: topo -> 4 -> 3 -> 2 -> 1 -> 

# Segunda etapa (pilha -> fila):
  Pop() = 4, Enqueue(4) -> fila: inicio -> 4 -> 
  Pop() = 3, Enqueue(3) -> fila: inicio -> 4 -> 3 -> 
  Pop() = 2, Enqueue(2) -> fila: inicio -> 4 -> 3 -> 2 -> 
  Pop() = 1, Enqueue(1) -> fila: inicio -> 4 -> 3 -> 2 -> 1 -> 

# Resultado: <4, 3, 2, 1>, exatamente a fila invertida'''

'''b) Tempo de execução: O(n), o algoritmo realiza n inserções/remoções
na primeira etapa e n na segunda etapa'''
'''c)Sim. É possível inverter a ordem mantendo 
exatamente os mesmos nós em memória, apenas 
manipulando os ponteiros de encadeamento simples'''