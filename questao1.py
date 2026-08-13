class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class pilhaencadeada:
    def __init__(self):
        self.topo = None
        
    def push(self, valor):
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo
    
    def pop(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        valor = removido.valor
        del removido #liberando a memoria
        return valor

#a)
'''topo ---> [ 3 | • ] ---> [ 99 | • ] ---> [ 42 | • ] ---> [ 17 | • ] ---> [ 5 | / ]
'''
#b) 
'''Primeiro pop:
valor removido = 3
pilha resultante: topo ---> [ 99 | • ] ---> [ 42 | • ] ---> [ 17 | • ] ---> [ 5 | / ]

Segundo pop: 
valor removido = 99
pilha resultante: topo ---> [ 42 | • ] ---> [ 17 | • ] ---> [ 5 | / ]
'''
#Tempo de execução do push = O(1)
#Tempo de execução do pop = O(1)

#c) 
'''Para atualizar o ponteiro topo para o proximo elelemnto,
é necessario ler o ponteiro proximo contido no nó atual do topo'''
'''Se o nó do topo fosse deletado primeiro o acesso ao ponteiro proximo
causaria um erro de acesso inválido à memória. Perderia a referência para onde 
está o restante da pilha'''
