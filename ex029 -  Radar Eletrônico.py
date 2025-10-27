v = int(input("Digite sua velocidade: "))

if v > 80:
    m = (v - 80) * 7
    print("Você passou do limite de velocidade permitida.")
    print(f"Sua multa é de R${m}")
    
else:
    print("Você está dentro do limite")
