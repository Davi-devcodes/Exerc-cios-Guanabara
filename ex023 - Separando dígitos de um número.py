n = int(input("Digite um número de 0 a 9999: "))
uni = n % 10
des = (n // 10) % 10
cen = (n // 100) % 10
mil = (n // 1000) % 10

print(f"Milhar: {mil}")
print(f"Centena: {cen}")
print(f"Dezena: {des}")
print(f"Unidade: {uni}")
