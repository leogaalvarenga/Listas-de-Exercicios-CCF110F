tam = 10
n = [[0 for i in range(tam)] for j in range(tam)]
for i in range(tam):
    for j in range(tam):
        n[i][j] = int(input())
for i in range(tam):
    for j in range(tam):
        if i ==j:
            print(n[i][j])