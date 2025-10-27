num = []
n = 0 
p = None

while p != 'N':
    n = int(input('Digite um valor: '))
    p = str(input('Você quer continuar[S/N]? ')).upper()
    num.append(n)

soma = sum(num)  
qtd = len(num)
maior = max(num)
menor = min(num)
media = soma / qtd

print('\nA média desses números é', media)
print(f'O maior valor é {maior} e o menor é {menor}.')





    
