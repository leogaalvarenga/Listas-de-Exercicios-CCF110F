n = [[0 for i in range(10)]for j in range(10)]
for i in range(10):
    for j in range(10):
        n[i][j] = int(input())
        if j > i:
            print(n[i][j])
