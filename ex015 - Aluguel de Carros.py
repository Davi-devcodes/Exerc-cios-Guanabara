d = int(input("Quantos dias seu carro está alugado? "))
k = float(input("Quantos km rodados? "))
c = (60 * d) + (k * 0.15)
print(f"O preço  pagar pelo carro alugado é R${c:.2f}")
