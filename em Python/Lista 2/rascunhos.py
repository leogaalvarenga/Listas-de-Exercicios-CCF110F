soma = 0
m = 1
n = 25
x = int(input())
for i in range(1, 25):
    div = (x**n) / m
    if m % 2 == 0:
        soma -= div
    else:
        soma += div
    m += 1
    n -= 1
print(soma)