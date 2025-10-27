maiorid = 0
homi = 0
mulher = 0

while True:
    print('\nCadastre uma pessoa')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo[M/F]: ')).upper()
    if idade >= 18:
        maiorid += 1
    if sexo == 'M':
        homi += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    escolha = str(input('Quer cadastrar mais alguém? ')).upper()
    if escolha == 'N':
        break

print('\nTotal de pessoas com mais de 18 anos:', maiorid)
print('Total de homens cadastrados:', homi)
print('Total de mulheres com menos de 20 anos', mulher)





    
