soma = 0
A = [[int(input()) for j in range(5)] for i in range(4)]
for i in range(4):
    for j in range(5):
        soma += A[i][j]
print(soma)