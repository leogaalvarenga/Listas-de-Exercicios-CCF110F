soma = 0
n = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        n[i][j] = int(input())
        if j > i:
            soma += n[i][j]
    print(soma)
# for i in range(10):
#     for j in range(10):
