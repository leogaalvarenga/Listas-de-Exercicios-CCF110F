nume = 480
deno = 10
soma = 0
for i in range(30):
    div = (nume / deno)
    if deno % 2 != 0:
        soma -= div
    else:
        soma += div
    nume -= 5
    deno += 1
print("O resultado da soma é {}".format(soma))