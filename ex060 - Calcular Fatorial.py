r = 1

n = int(input('Digite um número: '))
fatorial = n

print(f'{fatorial}! = ', end=" ")

while n >= 1:
     print(n, end='')
     print(' x ' if n > 1 else ' = ', end="")
     r *= n   
     n -= 1


print(r, end=" ")

