l = []
i = 0

while True:
    n = int(input('Digite um valor ou -1 para parar: '))
    if n == -1:
        break
    if n in l:
        print('Esse valor já foi adicionado')
    else:
        l.append(n)
        l.sort(reverse=True)
    

print(l)

print(f'Foram digitados {len(l)} números.')

ve = 5 in l
if ve == False:
    print('O número 5 não foi digitado')

else:
    print('O número 5 foi digitado')





    



