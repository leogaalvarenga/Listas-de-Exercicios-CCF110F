N = int(input())
for i in range(N):
    if i == 2 or i == 3 or i ==5 or i == 7:
        print(i)
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
    else:
        continue