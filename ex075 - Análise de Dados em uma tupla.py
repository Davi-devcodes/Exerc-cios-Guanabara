n = ()

for c in range(4):
    n += (int(input('Digite um valor: ')),)

nove = n.count(9)
par = ()

for p in n:
    if p % 2 == 0:
       par += (p,)



print('Você digitou os numeros:',n)
print(f'O nove apareceu {nove} vezes')
print('Números pares encontrados:', *par, sep=' ')

if 3 in n:
    print('O três está na posição', n.index(3) + 1)
else:
    print('O 3 não está na lista')
    
