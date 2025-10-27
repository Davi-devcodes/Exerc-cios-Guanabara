s = float(input("Digite seu salário: "))
if s > 1250.00:
    t = 10/100 * s
    sf = s + t
    print(f"Seu salário com aumento de 10%, é de {sf:.2f}")

else:
    t = 15/100 * s
    sf = s + t
    print(f"Seu salário, com aumento de 15%, é de {sf:.2f}")
