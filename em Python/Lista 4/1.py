a1 = int(input("Insira o primeiro termo:\n"))
r = int(input("Insira a razao da PA:\n"))
n = int(input("Insira o termo que vc deseja: \n"))
a = a1 + (n - 1)*r
print("O termo na posição %s é: %s."%(n, a))