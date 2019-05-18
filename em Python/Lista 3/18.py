for i in range(5):
    a, b = map(int, input().split())
    if a < b:
        if a % 2 == 0:
            print(a)
        else:
            a += 1
    else:
        break
