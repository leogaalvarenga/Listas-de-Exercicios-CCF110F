n = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        n[i][j] = int(input())

        if i != j:
            print(n[i][j])
# for i in range(10):
#     for j in range(10):