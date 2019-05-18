linha = 3
coluna = 3

N = int(input('Quantos graus voce deseja rotacionar a matriz?\n'))
m = [[int(input()) for j in range(coluna)] for i in range(linha)]
m1 = m
# N equivale ao numero de rotacoes no sentido horario, como sabemos, a cada 90 graus, rodamos a matriz uma vez
# como demosntrado abaixo
if N == 90:
    N = 1
elif N == 180:
    N = 2
elif N == 270:
    N = 3
elif N == 360:
    print(m1)
else:
    N = 0
    print("Valor invalido.")
for i in range(N):
    m1 = list(zip(*reversed(m1)))
# O professor de prog nao apoia o uso de funcoes prontas , portanto essa resoluçao nao e valida para seus padroes
print(m1)

# for i in range(linha):
#     for j in range(coluna):
        # m[i][j] = m[linha - j -1][i]