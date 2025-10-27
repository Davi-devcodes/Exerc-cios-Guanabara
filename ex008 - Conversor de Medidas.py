print("CONVERSOR DE MEDIDA")
n = float(input("Digite um valor em metros: "))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print(f"{n} m, são {km} km")
print(f"{n} m, são {hm} hm")
print(f"{n} m, são {dam} dam")
print(f"{n} m, são {dm} dm")
print(f"{n} m, são {cm} cm")
print(f"{n} m, são {mm} mm")
