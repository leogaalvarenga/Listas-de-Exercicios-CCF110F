n = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        n[i][j] = int(input())
        if i + j > 10:
            print(n[i][j])