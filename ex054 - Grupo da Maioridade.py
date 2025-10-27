tm = 0
tmn = 0

for c in range(1,8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = 2025 - ano

    if idade >= 21:
        tm += 1

    else:
        tmn += 1

print(f'Ao todo tivemos {tm} pessoas de maior idade\nE {tmn} pessoas de menor idade')


