N = int(input())
n = []
for i in range(N):
    a = int(input())
    n.append(a)
K = int(input())
print(n[K])
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j+1], n[j] = n[j], n[j+1]
print(n[K])