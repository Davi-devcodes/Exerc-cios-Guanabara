u = input('Digite a expressão: ')
pilha = []
for símb in u:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta')
else:
    print('A expressão está errada')
