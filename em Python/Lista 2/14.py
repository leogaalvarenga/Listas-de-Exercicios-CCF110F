n = int(input("Insira seu numero: \n"))
n1 = n - 1

if n == 0:
    print("O fatorial de 0 é 1, bobinho.")
else:
    while n1 not in [1]:
        n1 -= 1
        nfato = n * n1
    print(nfato)