NUM = int(input())
for i in range(1, NUM):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    else:
        continue