n1 = 0
n2 = 0
for i in range(10):
    n = float(input())
    if n > 10 and n <= 20:
        n1 += 1
    else:
        n2 += 1
print(n1, n2)