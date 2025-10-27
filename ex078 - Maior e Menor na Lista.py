num = []
cont = 0

while cont < 5:
    n = int(input('Digite um valor: '))
    cont += 1
    num.append(n)

maior = max(num)
menor = min(num)

print('Você digitou os valores:', num)
print(f'O maior valor digitado foi {maior} e ele está na posição', num.index(maior) + 1)
print(f'O menor valor digitado foi {menor} e ele está na posição', num.index(menor) + 1)
