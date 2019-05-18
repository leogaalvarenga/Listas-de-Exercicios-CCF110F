n = [0 for i in range(10)]
for i in range(10):
    A = int(input())
    if n[i] != A:
        n[i] = A
for j in range(10):
    if n[j] > 0:
        print(n[j], end=' ')