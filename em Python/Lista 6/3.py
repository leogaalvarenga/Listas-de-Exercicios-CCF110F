n = [0 for i in range(10)]
n1 = []
for i in range(10):
    n[i] = int(input())
    n1 = n
for j in range(10):
    if n[j] < 10:
        n[j] = j
print(n)
print(n1)