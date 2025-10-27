nt1 = float(input("Digite sua primeira nota: "))
nt2 = float(input("Digite sua segunda nota: "))
md = (nt1 + nt2)/2
print(f"Sua média é {md:.1f}")

if md < 5:
    print("REPROVADO")

elif md > 5.0 and md < 6.9:
    print("RECUPERAÇÃO")

else:
    print("APROVADO")
