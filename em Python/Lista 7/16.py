n = [[0 for j in range(3)] for i in range(50)]
eideal = [[0 for l in range(1)] for k in range(50)]
for i in range(2):
    a, b, c = input("Insira o nome do produto, seu estoque ideal e seu estoque atual:\n").split(' ')
    a, b, c, = str(a), int(b), int(c)
    n[i][0], n[i][1], n[i][2] = a, b, c
    if c - b < 0:
        eideal[i][0] = (c-b)
    else:
        eideal[i][0] = 0
for i in range(2):
    if eideal[i][0] < 0:
        eideal[i][0] *= -1
        print("Voce deve comprar %d %s" % (eideal[i][0], n[i][0]))