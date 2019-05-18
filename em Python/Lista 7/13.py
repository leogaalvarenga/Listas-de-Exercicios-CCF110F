A = [[int(input()) for j in range(5)] for i in range(5)]
B = [[int(input()) for l in range(5)] for k in range(5)]

for i in range(5):
    for j in range(5):
        A[i][j] -= B[i][j]
print(A)