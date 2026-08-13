class No:
    def __init__(self, dado: int, min_atual: int):
        self.dado = dado
        self.min_atual = min_atual  #Guarda o menor valor da pilha até este nó
        self.proximo = None

class PilhaComMin:
    def __init__(self):
        self.topo = None

    def push(self, x: int) -> None:
        #se a pilha estiver vazia o mínimo é o próprio x.
        #caso contrário o mínimo é o menor entre x e o mínimo do topo atual.
        if self.topo is None:
            novo_min = x
        else:
            novo_min = min(x, self.topo.min_atual)
            
        novo_no = No(x, novo_min)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self) -> int:
        if self.topo is None:
            return None
        no_removido = self.topo
        self.topo = self.topo.proximo
        return no_removido.dado

    def get_min(self) -> int:
        if self.topo is None:
            return None
        return self.topo.min_atual

'''a) Cada nó deve conter 3 campos:
1. dado(valor): aramazena o valor do elemento inserido no nó
2. min_atual(minimo corrente): aramazena o menor elemento presente na pilha no momneto
em que esse nó foi empilhado
3. proximo(ponteiro): aponta para o nó imediatamente abaixo da pilha'''

'''b)Push(topo, valor):
     novoNode.valor <- valor
     se topo = nulo:
         novoNode.min_atual <- valor
     senão:
         novoNode.min_atual <- min(valor, topo.min_atual)
     novoNode.proximo <- topo
     topo <- novoNode

# Pop(topo):
     se topo = nulo:
         retorna erro (pilha vazia)
     noRemovido <- topo
     topo <- topo.proximo
     noRemovido.proximo <- nulo
     retorna noRemovido.valor

# Min(topo):
     se topo = nulo:
         retorna erro (pilha vazia)
     retorna topo.min_atual'''

'''c)
   Push(5) -> topo 5(min=5) -> /
   Push(3) -> topo 3(min=3) -> 5(min=5) -> /
   Push(7) -> topo 7(min=3) -> 3(min=3) -> 5(min=5) -> /
   Push(1) -> topo 1(min=1) -> 7(min=3) -> 3(min=3) -> 5(min=5) -> /
   Pop     -> remove 1, sobra topo 7(min=3) -> 3(min=3) -> 5(min=5) -> /
   Min     -> 3 (lido diretamente de topo.minimoAteAqui)'''

'''d) Complexidade de espaço extra: O(n)
'Cada um dos n nós da pilha precisa armazenar um inteiro a mais. 
Portanto, há um custo adicional 
fixo proporcional à quantidade de elementos armazenados na pilha.'''