n = [0 for i in range(20)]
for i in range(20):
    n[i] = int(input())
n1 = n
n2 = n
count = 19
for j in range(20):
    n1[count] = n[j]
    count -= 1
print(n1)