pt = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razão da PA: "))

contador = 0
total = 0
termos = 9

while termos!= 0:
    total = total + termos
    while total >= contador:
        t = pt + contador * r
        contador += 1
        print(t, end=' , ')
    print('Pausa')
    termos = int(input('Quantos termos você quer adicionar? '))

print('Fim')





    
    
    
