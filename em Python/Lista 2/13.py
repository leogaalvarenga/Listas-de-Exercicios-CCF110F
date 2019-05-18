ini = 1
valor = 0
valorf = 0

for i in range(62):
    ini += 1
    valor = pow(2, ini)
    print("Valor da casa atual: {}".format(valor))
    valorf += (valor + 3)
print("Valor final do processo: {}".format(valorf))
