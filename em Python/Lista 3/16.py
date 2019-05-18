n = int(input())
ini = 1
for i in range(1, n):
    print(ini, "X n =", ini*n)
    ini += 1
    if ini == n:
        print("n x n =", ini*n)
    elif ini > n:
        break