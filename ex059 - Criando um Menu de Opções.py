n = 0
menu = ''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))

while menu != '5':  
    menu = input('''\nMENU:
    1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - sair
    \nO que você quer fazer com esses dois números? ''')

    if menu == '1':
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')

    elif menu == '2':
         m = n1 * n2
         print(f'{n1} x {n2} = {m}')

    elif menu == '3':
        if n1 > n2:
            print('O primeiro valor é maior')
        elif n2 > n1:
            print('O segundo é maior')
        else:
            print('São iguais')

    elif menu == '4':
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite um número: '))
        
        

print('Saindo')
        
               



