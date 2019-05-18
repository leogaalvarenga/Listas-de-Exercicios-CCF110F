k = int(input("Insira um termo qualquer:\n"))
q = int(input("Insira a razao da PA:\n"))
n = int(input("Insira o termo que vc deseja: \n"))

a = k * (pow(q, (n - k)))
print("O termo na posição %s é: %s."%(n, a))