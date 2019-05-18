soma = 0
n = int(input())
x = [0 for i in range(n)]
for i in range(n):
    x[i] = float(input())
    if i % 2 == 0:
        soma += x[i]
print(soma)