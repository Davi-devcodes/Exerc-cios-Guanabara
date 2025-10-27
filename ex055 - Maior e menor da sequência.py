maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))

    if peso > maior:
        maior = peso

    else:
        if peso < maior:
            menor = peso

print(f'O maior peso é {maior}kg')
print(f'O menor peso é {menor}kg')
