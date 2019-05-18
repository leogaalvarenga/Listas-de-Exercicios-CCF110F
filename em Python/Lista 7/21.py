# N = int(input('Quantos graus voce deseja rotacionar a matriz?\n'))
m = [[int(input()) for j in range(3)] for i in range(3)]
m1 = m
# if N == 90:
#     N = 1
# elif N == 180:
#     N = 2
# elif N == 270:
#     N = 3
# else:
#     N = 0
#     print("Valor invalido.")
# for i in range(N):
#     m1 = list(zip(*reversed(m1)))
# print(m1)

m[0][2], m[2][2], m[2][0], m[0][0] = m[0][0], m[0][2], m[2][2], m[2][0]
m[1][2], m[2][1], m[1][0], m[0][1] = m[0][1], m[1][2], m[2][1], m[1][0]
print(m)