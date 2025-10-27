print("Calculadora de IMC - Índice de Massa Corporal")

# Interação com o usuário
p = float(input("Digite seu peso: "))
h = float(input("Digite sua altura: "))

# Cálculo do IMC
imc = p / h**2

# Resultado do IMC
print(f"Seu IMC é {imc:.1f}")

# Condições do IMC
if imc < 18.5:
    print("Você está abaixo do peso")

elif imc <= 25:
    print("Você está no peso ideal")

elif imc <= 30:
    print("Você está no sobrepeso")

elif imc <=40:
    print("Você está com obesidade")

elif imc > 40:
    print("Você está com Obesidade mórbida")



