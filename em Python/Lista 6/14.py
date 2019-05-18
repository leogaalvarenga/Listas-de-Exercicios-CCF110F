n1 = []
n2 = []
c = 0
N = int(input("Insira o numero de termos a serem inseridos:\n"))
n3 = [0 for i in range((N * 2))]
print("Vetor 1:\n")
for i in range(N):
    a = int(input())
    n1.append(a)
print("Vetor 2:\n")
for i in range(N):
    a = int(input())
    n2.append(a)
for i in range(N):
    n3[c] = n1[i]
    c += 2
c = 1
for i in range(N):
    n3[c] = n2[i]
    c += 2
print(n3)