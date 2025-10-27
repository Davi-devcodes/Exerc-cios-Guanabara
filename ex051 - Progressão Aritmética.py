pt = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razão da PA: "))

for c in range(0, 10):
    t = pt + c * r
    print(f"{t}", end=" , ")
