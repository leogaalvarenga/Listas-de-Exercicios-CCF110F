n = int(input("Quantos"))
for i in range(n):
    nome = str(input(""))
    n1, n2, n3, n4, n5 = input().split(" ")
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    n5 = float(n5)
    if (n1 >= 7 and n2 >= 7 and n3 >= 7 and n4 >= 7 and n5 >= 7):
        print("alunos aprovados em :\n", nome)
    elif (n1 >= 7 and n4 >= 7):
        print(nome)
    elif (n3 >= 7):
        print(n3*10, "%")