numeros = []
c = 0
while True:
    n = int(input('Digite um número ou -1 para parar: '))
    if n == -1 :
        break
    else:
        c += 1
        numeros.append(n)
        
pares = []
impares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
                

print('PARES:', pares)
print('ÍMPARES:', impares)
print('GERAL:', numeros)
