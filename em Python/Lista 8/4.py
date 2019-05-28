a1, a2 = map(int, input().split())
l1 = [int(input()) for i in range(a1)]
l2 = [int(input()) for i in range(a2)]
lista_intercalada = []

for i in range(max(a1, a2)):
    if i < a1:
        lista_intercalada.append(l1[i])
    if i < a2:
        lista_intercalada.append(l2[i])
print(lista_intercalada)
