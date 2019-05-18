m = []
n = []
N = int(input())
for i in range(N):
    a = int(input())
    n.append(a)
m = n
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j + 1], n[j] = n[j], n[j+1]
print(n)
for i in range(len(m)):
    for j in range(len(m)-1):
        if n[j] < n[j+1]:
            m[j+1], m[j] = m[j], m[j+1]
print(m)