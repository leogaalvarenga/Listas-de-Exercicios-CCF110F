den = 1
num = 38
div = 0
soma = 0
for i in range(38):
    if num > 1:
        num -= 2
        den += 1
        div = num * (num + 1) / den
        soma += div
    else:
        break