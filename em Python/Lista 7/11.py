A = [[int(input()) for j in range(4)] for i in range(3)]
B = [[0 for l in range(4)] for k in range(3)]

for i in range(3):
    for j in range(4):
        B[i][j] = (A[i][j] * 3)
print(B)