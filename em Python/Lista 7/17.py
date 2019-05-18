n = [[int(input()) for j in range(2)] for i in range(5)]
sal = []
a = 0.0
b = 0.0
c = 0.0
soma = 0
for i in range(5):
    if a > b:
        c = a - b
        c, a = a, c
        c *= 10.0
        soma += 0.5 * ((b*15.0) + (a * 30.0) + c)
    else:
        c = b - a
        c, b = b, c
        c *= 15.0
        soma += 0.5 * ((a*10.0) + (b * 30.0) + c)
    sal.append(soma)
    soma = 0
    print("Manicure %d: R$ %.2f" % (i, sal[i]))