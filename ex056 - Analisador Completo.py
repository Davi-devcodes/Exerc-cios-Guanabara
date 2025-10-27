si = 0
mu = 0
maioridade = 0
nomev = ''

for c in range (1, 5):
    print(f'\n{c}ª pessoa')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    si += idade

    if sexo in 'M' and idade > maioridade:
        maioridade = idade
        nomev = nome

    elif sexo in 'F' and idade < 20:
        mu += 1
           
media = si/4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho é o {nomev}, que tem {maioridade} anos')
print(f'Possui {mu} mulheres com menos de 20 anos')


