def buscabinaria(inicio, fim,vetor, k):
    
    if inicio > fim:
        return -1
    
    meio = (inicio + fim)//2
    if vetor[meio] == k:
        return meio
    elif vetor[meio] < k:
        return buscabinaria(meio+1, fim, vetor, k)
    else:
        return buscabinaria(inicio, meio-1, vetor, k)
        
'''1. O tamanho da entrada é n elementos, ou seja, n = inicio + fim - 1
   2. Comparação de parada: if inicio > fim: 
      Cálculo do ponto médio: meio = (inicio + fim)//2
      Comparação do elemento: if vetor[meio] == k: elif vetor[meio] < k:
    Todas essas operações levam um custo constante, ou seja, O(1)
   3. Tempo de execução: O(1) + O(log n) = O(log n)
   4. Descartamos as constantes e pegamos a expressão dominante, log n.
   Portanto o custo é O(log n)
      '''        
lista=[1,2,3,5,6,8,9]
x=buscabinaria(0,len(lista)-1,lista,8)
print(x)
