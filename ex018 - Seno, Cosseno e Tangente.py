import math
n = float(input("Digite o valor do ângulo: "))
ng = math.sin(math.radians(n))
ng2 = math.cos(math.radians(n))
ng3 = math.tan(math.radians(n))
print(f"O seno desse ângulo é {ng:.2f}, o cosseno é {ng2:.2f} e tangente é {ng3:.2f}")
