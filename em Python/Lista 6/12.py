n = [0 for i in range(10)]
n1 = [0 for j in range(10)]
for i in range(10):
    n[i] = int(input())
for j in range(10):
    n1[j] = n[9 - j]
print(n)
print(n1)