import random

print("JOKENPÔ\n")

# Computador escolhe
ppt = ["pedra", "papel", "tesoura"]
ce = random.choice(ppt)
print("Já escolhi o meu. Agora é sua vez!")

# Usuário escolhe
es = input("Pedra, papel ou tesoura? " ).lower()

# Situação de Empate
if ce == es:
    print(f"Eu também escolhi {ce}")
    print("Empatamos")

# Situação de vitória do usuário    
elif (es == "pedra" and ce == "tesoura") or \
     (es == "papel" and ce == "pedra") or \
     (es == "tesoura" and ce == "papel"):
    print(f"Eu escolhi {ce}")
    print("Você venceu")

# Situação de derrota do usuário
elif (ce == "pedra" and  es == "tesoura") or \
     (ce == "papel" and es == "pedra") or \
     (ce == "tesoura" and es == "papel"):
    print(f"Eu escolhi {ce}")
    print("Você perdeu")

else:
    print("Jogada inválida")






