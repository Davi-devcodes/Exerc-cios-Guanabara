numeros = ('zero','um' , 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

digitar = int(input('Digite um número entre 0 e 20: '))

while digitar < 0 or digitar > 20:
    digitar = int(input('Tente novamente. Digite um número entre 0 e 20: '))

ler = numeros[digitar]
print('Você digitou o número', ler)
