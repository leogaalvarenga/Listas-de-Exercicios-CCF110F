n = []
for i in range(10):
    x = int(input())
    n.append(x)
a = int(input())
for j in range(30):
    print("%d X %d = %d" %(n[j], a, (n[j] * a)))
    if (n[j] * a) % 2 == 0:
        print("E par")
    else:
        print("Nao e par")