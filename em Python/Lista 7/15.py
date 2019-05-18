A = [[int(input()) for j in range(5)] for i in range(3)]
SL = [0]*3
for i in range(3):
    for j in range(5):
        SL[i] += A[i][j]
print(SL)