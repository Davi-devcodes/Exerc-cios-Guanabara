f = input("Digite uma frase: ").upper()
a = f.count('A')
print(f"A letra A aparece {a} vez(es)")
pi = f.find("A")+1
print(f"A primeira letra A apareceu na posição {pi}")
pf = f.rfind("A")+1
print(f"A última letra A apareceu na posição {pf}")

