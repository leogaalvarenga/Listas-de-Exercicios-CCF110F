k = int(input("Insira um termo qualquer:\n"))
r = int(input("Insira a razao da PA:\n"))
n = int(input("Insira o termo que vc deseja: \n"))

a = k + (n - k)*r

print("O termo na posição %s é: %s."%(n, a))