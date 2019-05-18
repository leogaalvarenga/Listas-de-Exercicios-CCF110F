contaimpares = 0
contapares = 0

for i in range(200):
    n = int(input("Insira seu numero: \n"))
    if n % 2 == 0:
        contapares += 1
    else:
        contaimpares += 1
print("Houveram {} numeros pares.".format(contapares))
print("Houveram {} numeros impares.".format(contaimpares))
