def inverter(frase: str):
    pilha = []
    final = ""
    
    for i in frase:
        if i != " ":
            pilha.append(i)
        else:
            while len(pilha)>0:
                final = final + pilha.pop()
            final = final + " "
    while len(pilha)>0:
        final = final + pilha.pop()
    return final        

print(inverter("Lissandra"))