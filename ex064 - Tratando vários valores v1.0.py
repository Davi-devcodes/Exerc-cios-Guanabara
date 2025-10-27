n = []
s = 0
v = None

while v != 999:
    v = int(input('Digite um número: '))
    if v != 999:
        n.append(v)
        s += v
         
qtd = len(n)
print(f'Foram digitados {qtd} números')
print('A soma entre eles é', s)

    
