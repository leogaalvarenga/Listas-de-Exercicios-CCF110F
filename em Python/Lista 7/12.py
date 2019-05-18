A = [[int(input()) for j in range(4)] for i in range(4)]
B = [[int(input()) for l in range(4)] for k in range(4)]

for i in range(4):
    for j in range(4):
        B[i][j] += A[i][j]
print(B)