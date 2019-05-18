N = int(input())
n = int(input())
n2 = int(input())
c = 0
for i in range(N):
    c = n + n2
    n2 = n
    n = c
    print(c)