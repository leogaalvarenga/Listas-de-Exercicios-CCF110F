for a in range(3):
    n = int(input("numero"))
    if a == 0:
        maior = n
        menor = n
    elif (n > maior):
        maior = n
print(maior, menor)