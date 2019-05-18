soma = 0
po = 0
ne = 0
for i in range(10000):
    n = int(input())
    nome = str(input())
    saldo = float(input())
    if saldo < 0:
        ne += 1
        print("Saldo {} \n negativo" .format(saldo))
    elif saldo == -999 or nome == -999 or n == -999:
        break
    soma += saldo
print("Total de clientes: %d" % (po + ne))
print("Saldo da Agencia: %d" % soma)
print("Clientes positivos: %d\nClientes negativos: %d" % (po, ne))