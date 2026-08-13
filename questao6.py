class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def push(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def pop(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return removido.dado

    def is_empty(self):
        return self.topo is None


class FilaComDuasPilhas:
    def __init__(self):
        self.p1 = PilhaEncadeada()  # Pilha de entrada
        self.p2 = PilhaEncadeada()  # Pilha de saída

    def enqueue(self, x: int) -> None:
        """Tempo de execução: O(1)"""
        self.p1.push(x)

    def dequeue(self) -> int:
        """Tempo de execução: O(1) amortizado (pior caso $O(n)$)"""
        if self.p2.is_empty():
            # Transfere todos os elementos de P1 para P2
            while not self.p1.is_empty():
                self.p2.push(self.p1.pop())
                
        if self.p2.is_empty():
            return None  # Fila totalmente vazia
            
        return self.p2.pop()

'''a)
#Enqueue(x): 
     Insere o elemento x diretamente no topo de P1.
     Tempo de execução: O(1). 
#Dequeue():
    Se P2 estiver vazia, desempilha todos os elementos de P1 um por um e os empilha em P2.
    Em seguida, realiza o pop() de P2.
    Tempo de execução: O(1) amortizado.'''

''' (b) O custo amortizado de Dequeue é O(1), mesmo que uma chamada individual possa
# custar O(n) (quando P2 está vazia e é preciso transferir todos os elementos de
# P1). Usando o método do potencial, definimos Φ = número de elementos em P1
# (Φ >= 0 sempre, e Φ inicial = 0, então a soma dos custos amortizados nunca fica
# abaixo da soma dos custos reais, garantindo que a análise é válida).
#
#   Enqueue: o custo real é O(1) (um único Push em P1), e Φ aumenta em 1 (mais um
#   elemento em P1). Custo amortizado = custo real + ΔΦ = O(1) + O(1) = O(1).
#
#   Dequeue quando P2 não está vazia: custo real O(1) (um único Pop em P2), e Φ não
#   muda (P1 não é tocada). Custo amortizado = O(1) + 0 = O(1).
#
#   Dequeue quando P2 está vazia e P1 tem k elementos: o custo real é O(k) (k Pops
#   em P1 seguidos de k Pushes em P2) mais O(1) do Pop final em P2, ou seja O(k+1).
#   Mas Φ diminui em k (P1 perde seus k elementos), então ΔΦ = -k. Custo amortizado
#   = O(k+1) - k = O(1).
#
# Em todos os casos o custo amortizado é O(1); o custo real de O(n) de uma
# transferência é "pago antecipadamente" pelo potencial acumulado pelos n Enqueues
# anteriores que colocaram os elementos em P1.'''

'''c)Sim, a propriedade FIFO (First-In, First-Out) é preservada.
Uma pilha funciona no formato LIFO (Last-In, First-Out). 
Quando invertemos a ordem dos elementos ao movê-los de P1 para P2 (desempilhando e reempilhando), a ordem LIFO aplicada duas vezes seguidas resulta na ordem original de chegada (FIFO). '''