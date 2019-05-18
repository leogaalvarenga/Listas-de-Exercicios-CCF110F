# dados = [[0 for j in range(4)] for i in range(10)]
# fem = [[0 for l in range(4)] for k in range(10)]
# for i in range(10):
#     for j in range(4):
#         dados[i][j] = int(input())
# for i in range(10):
#     for j in range(4):
#         if dados[i][1] ==  0:
#             fem[i][j] = dados[i][j]
# for i in range(10):
#     for j in range(9):
#         for k in range(4):
#             for l in range(3):
#                 if fem[i][3] > fem[i+1][3]:
#                     fem[i+1][j], fem[i][j] = fem[i][j], fem[i+1][j]
# print(fem)

dados = [[0 for j in range(4)] for i in range(2)]
fem = [[0 for l in range(4)] for k in range(2)]
for i in range(2):
    for j in range(4):
        dados[i][j] = int(input())
for i in range(2):
    for j in range(4):
        if dados[i][1] ==  0:
            fem[i][j] = dados[i][j]
for i in range(2):
    for j in range(1):
        for k in range(4):
            for l in range(3):
                if fem[i][3] > fem[i+1][3]:
                    fem[i+1][j], fem[i][j] = fem[i][j], fem[i+1][j]
print(fem)