l = []
cont = 0

while cont < 5:
    n = int(input('Digite um número: '))
    i = 0
    while i < len(l):
        if n in l:
            print('Esse valor já foi adicionado')
        elif n < l[i]:
            l.insert(i, n)
            break
        i += 1
    else:
        l.append(n)

    cont += 1
    
    
print(l)
