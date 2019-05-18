M = int(input())
A = []
B = []
for i in range(M):
    a = int(input())
    A.append(a)
N = int(input())
for i in range(N):
    b = int(input())
    B.append(b)
C = []
for i in range(len(B)):
    if B[i] in A and B[i] not in C:
        C.append(B[i])
print(A)
print(B)
print(C)