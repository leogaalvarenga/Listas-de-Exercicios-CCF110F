vezes = int(input("Quantos numeros voce deseja digitar? \n"))

maior = 0
for i in range(vezes):
    n = float(input("Insira um numero: \n"))
    if n > maior:
        maior = n
    else:
        continue
print("O maior numero digitado foi {}.".format(maior))