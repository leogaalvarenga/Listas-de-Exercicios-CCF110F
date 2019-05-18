# m = [[int(input()) for j in range(3)] for i in range(3)]
# m1 = m
# for i in range(2):
#     m1 = list(zip(*reversed(m1)))
# print(m1)

m = [[int(input()) for j in range(3)] for i in range(3)]
m[0][0], m[2][2] = m[2][2], m[0][0]
m[0][2], m[2][0] = m[2][0], m[0][2]
m[1][0], m[1][2] = m[1][2], m[1][0]
m[0][1], m[2][1] = m[2][1], m[0][1]
print(m)