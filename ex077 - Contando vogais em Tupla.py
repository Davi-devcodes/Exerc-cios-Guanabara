palavras = ('boi', 'carro', 'aprender')
vogais = ('a', 'e', 'i', 'o','u')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end=' ')
    for vogal in vogais:
        if vogal in palavra:
            print(vogal, end=' ')
