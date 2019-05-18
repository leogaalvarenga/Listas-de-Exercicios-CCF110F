neg = 0
n = 0
soma = 0
while 1:
    conta = int(input())
    saldo = float(input())
    soma += saldo
    n += 1
    print("Conta: %d\nSaldo: %d"% (conta, saldo))
    if saldo < 0:
        print("Saldo negativo")
        neg += 1
    else:
        print("Saldo positivo")
    if conta < 0:
        break
print("% de clientes negativos" %(neg*100))