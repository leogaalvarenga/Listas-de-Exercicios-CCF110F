A = [[int(input()) for j in range(2)] for i in range(2)]
a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]

ai = [[a, b], [c, d]]

ai[0][0] = d / (a * d - b * c)
ai[0][1] = -b / (a * d - b * c)
ai[1][0] = -c / (a * d - b * c)
ai[1][1] = a / (a * d - b * c)

print(ai)
# for i in range(2):
#     for j in range(2):
#         ai =