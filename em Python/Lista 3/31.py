n = int(input())
for i in range(n):
    nome = str(input())
    ncarros = int(input())
    valor = float(input())
    salario = (valor*0.05) + (50*ncarros) + 500
    print("O vendedor %s recebeu R$ %.2f" % (nome, salario))