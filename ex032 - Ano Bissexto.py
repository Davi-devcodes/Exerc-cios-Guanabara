import calendar
a = int(input("Digite um ano: "))
b = calendar.isleap(a)
if b == True:
    print("O ano é bissexto")

else:
    print('O ano não é bissexto')
