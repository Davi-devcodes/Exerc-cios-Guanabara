num = []

while True:
    n = input('Digite um valor. Caso não queira digitar, escreva PARAR: ')
    if n.upper() == 'PARAR':
        break
    else:
        n = int(n)
        if n in num:
            print(f'Não vou adicionar, pois já tem este valor na lista')
            num.remove(n)
            
        num.append(n)


crescente = sorted(num)
print(crescente)

