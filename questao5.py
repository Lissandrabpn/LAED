class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            return None
        no_removido = self.topo
        self.topo = self.topo.proximo
        return no_removido.dado

    def is_empty(self):
        return self.topo is None


def verificar_balanceamento(expressao: str) -> tuple[bool, str]:
    pilha = PilhaEncadeada()
    mapeamento = {')': '(', ']': '[', '}': '{'}
    abridores = {'(', '[', '{'}
    fechadores = {')', ']', '}'}

    for i, char in enumerate(expressao):
        if char in abridores:
            pilha.push(char)
        elif char in fechadores:
            if pilha.is_empty():
                return False, f"Erro no índice {i} ({char}): Fechador sem abridor correspondente na pilha."
            
            topo_val = pilha.pop()
            if topo_val != mapeamento[char]:
                return False, f"Erro no índice {i} ({char}): Fechador não combina com o abridor '{topo_val}' do topo."

    #se ao final a pilha não estiver vazia, sobrou algum abridor não fechado
    if not pilha.is_empty():
        return False, f"Erro no final da cadeia: Abridor '{pilha.topo.dado}' não foi fechado."

    return True, "Cadeia válida"
'''b)
#Complexidade de tempo: O(n) onde n é o comprimento da expressão
#Complexidade de espaço: O(n)'''

'''(c) Aplicando o algoritmo às cadeias do enunciado:
   ({[]})       -> válida: cada abridor é fechado na ordem correta.
   ({[)}]       -> inválida na posição 3 (caractere ')'): quando encontramos ')',
                   o topo da pilha é '[' (empilhado por causa do '[' na posição 2),
                   e ')' não é o fechador de '[', portanto o par está incorreto.
   ({[]}[()]{}) -> válida: cada abridor também é fechado na ordem correta.'''
