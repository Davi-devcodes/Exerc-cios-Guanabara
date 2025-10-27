t1 = float(input("Primeiro segmento: "))
t2 = float(input("Segundo segmento: "))
t3 = float(input("Terceiro segmento: "))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print("Os segmentos acima podem formar um triângulo")
    if t1 == t2 and t1 == t3:
        print("É um triângulo equilátero")

    elif t1 == t2 or t1 == t3 or t2 == t3:
        print("É um triângulo isóceles")

    else:
        print("É um triângulo escaleno")

else:
    print("Os segmentos acima não podem formar um triângulo")


