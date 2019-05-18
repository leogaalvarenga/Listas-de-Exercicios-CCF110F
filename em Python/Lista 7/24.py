m = [[0 for j in range(10)] for i in range(10)]
for j in range(9):
    m[2][j], m[2][j+1] = m[8][j], m[8][j+1]
for i in range(9):
    m[i][4], m[i+1][4] = m[i][10], m[i+1][10]
for i in range(10):
    for j in range(10):
        if i == j:
            if i >= 9 and j <= 9:
