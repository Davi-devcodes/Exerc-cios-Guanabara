cont = 0
s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n

print(f'Foram digitados {cont} números')
print(f'A soma entre eles é {s}')    
