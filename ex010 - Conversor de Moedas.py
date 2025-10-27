reais = float(input("Quanto dinheiro, em reais, você tem? R$ "))
c = 5.65
ce = 6.32
e = reais / ce
d = reais / c            
print(f"Com R${reais}, você consegue comprar US${d:.2f} e €{e:.2f}")           
