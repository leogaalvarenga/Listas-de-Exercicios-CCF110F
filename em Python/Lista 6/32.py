n = []
t = []
for i in range(10):
    a = int(input())
    b = int(input())
    n.append(a)
    t.append(b)
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j + 1]:
            n[j+1], n[j] = n[j], n[j+1]
        for k in range(len(t)-1):
            if t[k] > t[k+1]:
                t[k+1], t[k] = t[k], t[k+1]
for i in range(10):
    print("%d colocado: %d" %((i+1), t[9-1]))