ano = int(input("Digite seu ano de nascimento: "))
id = 2025 - ano
print(f"Você tem {id} anos")

if id < 10:
    print("Sua categoria é MIRIM")

elif id < 15:
    print("Sua categoria é INFANTIL")

elif id <19:
    print("Sua categoria é JUNIOR")

elif id == 20:
    print("Sua categoria é SÊNIOR")

elif id > 20:
    print("Sua categoria é MASTER")

else:
    print("Invalido")

