x = 0
n = []
nomes = []
while True:
    A = str(input())
    nomes.append(A)
    B1 = float(input())
    B2 = float(input())
    B3 = float(input())
    B4 = float(input())
    n.append(B1, B2, B3, B4)
    if A == 'sair':
        break
    x += 1
for i in range(x):
    print("Aluno: %s\n Nota: %d\n%d\n%d\n%d"%(nomes[i], n[i], n[i+1], n[i+2], n[i+3]))