B = []
A = []
for i in range(30):
    a = int(input())
    A.append(a)
    b = int(input())
    B.append(b)
x = int(input())
for i in range(len(A)):
    if A[i] == x:
        print(B[i])