notas = []
fa = [0 for i in range(2)]
for i in range(2):
    a = float(input())
    notas.append(a)
for i in notas:
    for notas[i] in notas:
        if notas[i] == notas[i + 1]:
            fa[i] += 1