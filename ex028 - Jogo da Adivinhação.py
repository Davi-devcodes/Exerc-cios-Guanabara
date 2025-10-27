import random

n = random.randint(0,5)
dn = int(input("Descubra o número de 0 a 5: "))


if dn == n:
    print('Você acertou')

else:
    print('Você errou')
