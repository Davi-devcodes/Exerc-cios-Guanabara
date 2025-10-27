import random

p = 0

cp = random.randint(0 ,10)
print('Pensei em um número. Agora, tente adivinhar')

jt = int(input('Qual número você acha que eu pensei? '))
p += 1

while jt != cp:
    print('Tente novamente')
    jt = int(input('Qual número você acha que eu pensei? '))
    p += 1

print(f'Você acertou! Precisou de {p} palpites pra acertar.')
