vdc = float(input("Qual o valor da casa? "))
sdc = float(input("Qual o salário do comprador? "))
t = float(input("Em quanto tempo ele vai pagar, em anos? "))

m = t * 12
pm = vdc / m

if pm > (30/100)*sdc:
    print("Empréstimo negado")

else:
    print("Empréstimo aceito")
