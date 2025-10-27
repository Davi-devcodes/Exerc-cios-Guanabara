n = int(input("Digite um número: "))
primo = True

if n < 2:
    primo = False
    
else:
    for c in range (2, n):
       if n % c == 0:
           primo = False
           break

if primo == False:
    print("Esse número não é primo")

else:
   print("Esse número é primo")


    
