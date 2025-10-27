pessoas = list()
nomes = list()
pesos = list()

while True:
    n = str(input('Digite o nome: '))
    if n.upper() == 'PARAR':
        break
    else:
        p = float(input('Digite o peso: '))
        nomes.append(n)
        pesos.append(p)
        pessoas.append(nomes)
        pessoas.append(pesos)
        
    
print(pessoas)
