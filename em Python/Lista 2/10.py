soma = 0
subtracao = 0
for i in range  (1, 52, 4):
    soma +=(1/pow(i, 3))
for j in range(3, 52, 4):
    subtracao -= (1/pow(j, 3))
total = soma + subtracao
pi = (total * 32) ** (1/3)
print(pi)