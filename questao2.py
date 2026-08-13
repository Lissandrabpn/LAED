class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
class Filanencadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def enqueue(self, valor): #enfileirar
        novo = No(valor)
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
    
    def dequeue(self): #desenfileirar
        if self.inicio is None:
            return None
        
        removido = self.inicio
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
        
        return removido.valor
#a) 
'''inicio ---> [ 8 | • ] ---> [ 15 | • ] ---> [ 23 | • ] ---> [ 7 | • ] ---> [ 11 | / ] <--- fim
'''
#Tempo de execução do enqueue = O(1)

#b)
'''Primeiro dequeue
valor removido = 8

Segundo dequeue
valor removido = 15

fila resultante:inicio ---> [ 23 | • ] ---> [ 7 | • ] ---> [ 11 | / ] <--- fim
'''

#c) 
'''Ao remover o unico elemento restante, o ponteiro inicio avança para seu proximo,
tornando-se None. Como a fila agora está vazia, o ponteiro fim deve ser atualizado
para None também '''
'''Ocorre uma inconsistência no estado da estrutura, ou seja, o ponteiro fim continuará
apontando para uma área de memoria de um nó que ja foi removido. Além disso, ao realizar
um novo enqueue, a verificação de fila vazia falhará se tnetar acessar fim.proximo, podendo tentar 
modificar um nó antigo'''