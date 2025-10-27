total = 0
caros = 0
barato = 1000
prod = ''
produtos = []

while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    produtos.append((produto, preco))
    for item in produtos:
        nome = item[0]
        preco = item[1]
        if preco < barato:
            barato = preco
            prod = nome
            
    total += preco
    if preco > 1000:
        caros += 1
    escolha = str(input('Vai querer contiunar?[S/N] ')).upper()
    if escolha == 'N':
        break


print('\nO total gasto foi: R$', total)
print(f'{caros} produtos custaram acima de R$1000,00.')
print(f'O produto mais barato foi o {prod} que custou R${barato}')

    
