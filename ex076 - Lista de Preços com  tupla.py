produtos = (('Pão', 0.30), ('Presunto', 25), ('Muçarela', 45.50), ('Bolos', 12))
print('-'*30)
print(' '* 10, end='')
print('PRODUTOS')
print('-'*30)

for produto, preco in produtos:
    print(f'{produto}..............R${preco:.2f}')

print('-'*30)

    
