import random

numeros = ()

for n in range(5):
    numeros += (random.randint(1, 100),)
    

menor = min(numeros)
maior = max(numeros)

print('Aqui está a tupla:', numeros)
print(f'O maior valor dessa tupla é {maior} e o menor é {menor}.')

