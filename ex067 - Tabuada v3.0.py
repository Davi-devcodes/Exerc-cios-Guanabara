while True:
    n = int(input('Você quer ver a tabuada de qual número? '))
    if n < 0:
        print('Programa Tabuada encerrado.')
        break
    else:
        cont = 0
        while cont < 10:
            cont += 1
            r = n * cont
            print(f'{n} x {cont} = {r}')
        
        
    
