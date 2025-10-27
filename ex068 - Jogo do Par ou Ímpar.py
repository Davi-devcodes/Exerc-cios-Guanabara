import random

print('Jogo Par ou Ímpar')

cont = 0

while True:
    n = int(input('\nDiga um número: '))
    poi = str(input('Par ou Ímpar[P/I]? ')).upper()
    pc = random.randint(1, 10)
    s = n + pc
        
    if s % 2 == 0 and poi == 'P':
        cont += 1
        print(f'Você jogou {n} e o computador {pc}. Total {s}. Deu par.')
        print('Você venceu!')

    elif s % 2 != 0 and poi == 'I':
        cont += 1
        print(f'Você jogou {n} e o computador {pc}. Total {s}. Deu ímpar.')
        print('Você venceu!')
        
    else:
        if s % 2 == 0 and poi == 'I':
            print(f'Você jogou {n} e o computador {pc}. Total {s}. Deu par.')
            print(f'\nVocê perdeu! Você só venceu {cont} vezes.')
            break
        
        elif s % 2 != 0 and poi == 'P':
            print(f'Você jogou {n} e o computador {pc}. Total {s}. Deu ímpar.')
            print(f'\nVocê perdeu! Você só venceu {cont} vezes.')
            break    
