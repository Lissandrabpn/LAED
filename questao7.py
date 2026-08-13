from typing import List
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class FilaEncadeada:
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


def radix_sort(lista: List[int]) -> List[int]:
    """
    Ordena uma lista de inteiros utilizando Radix Sort LSD com Filas Encadeadas.
    Tempo de Execução: O(d * (n + k)), onde d é o nº de dígitos e k a base (10).
    """
    if not lista:
        return []

    maior_valor = max(lista)
    exp = 1  # 1 para unidades, 10 para dezenas, 100 para centenas...

    # Cria 10 filas encadeadas (uma para cada dígito de 0 a 9)
    filas = [FilaEncadeada() for _ in range(10)]

    while maior_valor // exp > 0:
        # 1. Distribuição nas filas
        for num in lista:
            digito = (num // exp) % 10
            filas[digito].enqueue(num)

        # 2. Coleta das filas mantendo a ordem FIFO
        lista_ordenada = []
        for f in filas:
            while not f.is_empty():
                lista_ordenada.append(f.dequeue())

        lista = lista_ordenada
        exp *= 10

    return lista
'''a) Efeito: Pilhas operam no formato LIFO (Last-In, First-Out),
o que inverte a ordem relativa dos elementos que possuem o mesmo dígito em uma determinada passagem.
Essa inversão destrói a estabilidade da ordenação (garantia de que elementos com chaves iguais preservem sua ordem relativa inicial).
Como o Radix Sort LSD depende criticamente da estabilidade para que os 
dígitos mais significativos não desfaçam a ordenação dos menos significativos, o algoritmo falhará e retornará a lista desordenada.'''
'''Contra-exemplo concreto: considere apenas dois números de 2 dígitos,
        # 42 e 12, inseridos nessa ordem. O dígito menos significativo de ambos é 2.
        #
        # Com filas (FIFO), 42 entra primeiro na fila do dígito 2, e 12 entra depois.
        # Ao coletar, saem na mesma ordem em que entraram: 42, 12 — a ordem relativa
        # original entre eles foi preservada, que é exatamente a propriedade de
        # estabilidade de que o Radix Sort depende para os passos seguintes.
        #
        # Se usássemos uma pilha (LIFO) no lugar dessa fila, 42 (inserido primeiro)
        # ficaria no fundo, e 12 (inserido depois) ficaria no topo. Ao "coletar"
        # desempilhando, sairia primeiro 12 e depois 42 — a ordem relativa entre eles
        # foi invertida. Isso quebra a estabilidade: na passagem seguinte, o dígito
        # das dezenas depende de que números com o mesmo dígito das unidades
        # permaneçam na ordem em que chegaram (para que a passagem anterior continue
        # "valendo"), mas com pilhas essa ordem se perde a cada dígito empatado, e o
        # resultado final pode sair fora de ordem.'''
        
dados = [481, 329, 143, 612, 937, 480, 256]


resultado = radix_sort(dados)
print(f"RESULTADO FINAL ORDENADO: {resultado}") 

'''(c) Complexidade: para n strings (ou números) de comprimento fixo k sobre um
# alfabeto de tamanho sigma, cada passagem distribui os n elementos nas sigma
# filas (O(n)) e depois recolhe as sigma filas (O(n + sigma), pois é preciso
# visitar todas as sigma filas mesmo que algumas estejam vazias). Como existem k
# passagens (uma por posição), o tempo total do Radix Sort é O(k(n + sigma)).
# Quando sigma é uma constante (por exemplo, sigma = 10 para dígitos decimais),
# isso se reduz a O(kn).
#
# Comparando com o Merge Sort: ordenar n strings de comprimento k por comparação
# custa O(nk log n), pois cada uma das O(n log n) comparações entre duas strings
# pode custar até O(k) no pior caso (é preciso comparar caractere a caractere até
# encontrar uma diferença). Como o Radix Sort é O(kn), ele é assintoticamente
# melhor que o Merge Sort sempre que log n é maior que uma constante — ou seja,
# para n suficientemente grande o Radix Sort (O(kn)) vence o Merge Sort (O(kn log
# n)). A vantagem do Radix Sort é justamente evitar o fator log n; em troca, ele
# paga com a dependência de sigma (o tamanho do alfabeto) e com a exigência de que
# k seja fixo (ou conhecido de antemão), algo que o Merge Sort não precisa.'''
