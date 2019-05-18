N = int(input())
a = int(input())
b = int(input())
if N >= 3:
    for i in range(N):
        if i % 2 != 0:
            print((i-1) + (i-2))
        else:
            print((i-1) - (i-2))
else:
    print(" ")