dt = int(input("Digite o ano do seu nascimento: "))
id = 2025 - dt

if id > 18:
    tsm = dt + 18
    print(f"Já passou do tempo de você se alistar.\nVocê tinha que se alistar no ano {tsm}")

elif id < 18:
    tpm = dt + 18
    print(f"Você ainda vai se alistar. Você vai se alistar no ano {tpm} ")

else:
    print("Você se alista esse ano")
