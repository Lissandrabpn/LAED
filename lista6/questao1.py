def parenteses(expressao:str):
    pilha = []
    
    for i in expressao:
        if i=="(":
            pilha.append(i)
            print(pilha)
        elif i==")":
            if len(pilha)==0:
                return "Erro, ) não tem seu par correspondente"
        
            pilha.pop()
            print(pilha)
    if len(pilha)==0:
        return "Todos os parênteses tem seu par. Expressão balanceada"
    else:
        return "Expressão desbalanceada"

print("Teste 1:")
chamarfuncao = parenteses("(2+3)*5")
print(chamarfuncao)
print("Teste 2:")
chamarfuncao2 = parenteses("(2+5")
print(chamarfuncao2)
    
    