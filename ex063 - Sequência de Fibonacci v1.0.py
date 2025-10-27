sequencia = [0, 1]

n = int(input('Quantos termos você quer mostrar? '))

while len(sequencia) < n:
    ultimo = sequencia[-1]
    penultimo = sequencia[-2]
    proximo = penultimo + ultimo
    sequencia.append(proximo)
    
print(*sequencia, sep=' , ', end=' , ')
print('FIM')
