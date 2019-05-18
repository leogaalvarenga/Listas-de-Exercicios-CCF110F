p = int(input("Insira os numeros da placa: \n"))

mil = p // 1000
p -= (mil*1000)

cen = p // 100
p -= (cen*100)

dez = p // 10

print(dez)