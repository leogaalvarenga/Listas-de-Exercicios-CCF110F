N = int(input("Insira o tamanho da matriz:\n"))
a = [[int(input()) for j in range(N)] for i in range(N)]
at = [[0 for l in range(N)] for k in range(N)]
for i in range(N):
    for j in range(N):
        at[j][i] = a[i][j]
soma = 0
for i in range(N):
    for j in range(N):
        if a[i][j] == at[i][j]:
            soma +=1
if soma == (N**2):
    print("Matriz simetrica")
else:
    print("Matriz assimetrica")