s = float(input("Digite seu salário: R$ "))
op = input("Quer calcular aumento ou diminuição? ")
if op == "aumento":
 pa = float(input("Digite o valor do seu aumento: "))
 p = pa / 100
 a = p * s
 sf = s + a
 print(f"Com o aumento de {pa}%, seu salário de R${s:.2f}, agora é R${sf:.2f}")
elif op == "diminuição":
 pd = float(input("Digite o valor da sua diminuição: "))
 pc = pd / 100
 d = pc * s
 sf = s - d
 print(f"Com a diminuição de {pd}%, seu salário de R${s:.2f}, agora é R${sf:.2f}")
