x = [0 for i in range(5)]
y = [0 for i in range(5)]
for i in range(5):
    A = int(input())
    x.append(A)
for j in range(5):
    B = int(input())
    y.append(B)
z = [0 for i in range(5)]
for i in range(5):
    z[i] = x[i] + y[i]
print(z)
