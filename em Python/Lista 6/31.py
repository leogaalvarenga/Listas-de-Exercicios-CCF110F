count = {}
N = []
n = int(input())
for i in range(n):
    a = int(input())
    N.append(a)
for i in range(len(N)):
    for j in range(len(N)-1):
        if N[j] > N[j+1]:
            N[j+1], N[j] = N[j], N[j+1]
print(N)
for i in N:
    if i in count:
        count[i] += 1
    else:
        count[i] = i
for i in N:
    print(i, count[i])