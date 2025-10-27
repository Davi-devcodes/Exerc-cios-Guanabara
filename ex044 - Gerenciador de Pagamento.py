print("=-=-= Loja BIGODE =-=-=")

vdp = float(input("Qual o valor da compra? "))
cdp = input("Qual a forma de pagamento? ")

if cdp == "Cartão":
    vp = input("Vai parcelar? ")
    if vp == "Sim":
        vpv = int(input("Em quantas vezes? "))
        
        # Se ele parcelar em duas vezes, preço original
        if vpv == 2:
            print(f"Você vai pagar R${vdp:.2f}")
            
        # Se ele parcelar em mais, acrescenta-se mais 20% ao valor
        elif vpv >= 3:
            vj = 20/100 * vdp
            vf = vdp + vj
            print(f"Sua compra será parcelada em {vpv}x de R${vf:.2f} com juros")
            print(f"Você vai pagar R${vf:.2f} no final")
            
    # Se ele pagar a vista, ganha 5% de desconto        
    elif vp == "Não":
        vd = 5/100 * vdp
        vfd = vdp - vd
        print(f"Você vai pagar R${vfd:.2f}")

# Com dinheiro ou PIX, 10% de desconto
elif cdp == "Dinheiro" or cdp == "PIX":
    vcd = 10/100 * vdp
    vfcd = vdp - vcd
    print(f"Você vai pagar R${vfcd:.2f}")
