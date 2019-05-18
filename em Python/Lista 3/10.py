maior = 0
menor = 0
f = 0
m = 0
soma = 0
alturaf = 0
alturam = 0
for i in range(50):
    altura = float(input("Insira sua altura:\n"))
    genero = int(input("Insira um numero: \n 1 = masculino \n 2 = feminino:"))
    soma += altura
    if genero == 2:
         f += 1
         alturaf += altura
    else:
         m += 1
         alturam += altura
    if maior < altura:
        maior = altura
    if menor > altura:
        menor = altura
    else:
        continue
mediaf = alturaf/f

media = (alturaf + alturam)/(f + m)

print("Maior altura: %s; menor altura: %s"%(maior, menor))
print("Media feminina: {}".format(mediaf))
print("Media total: {}".format(media))
