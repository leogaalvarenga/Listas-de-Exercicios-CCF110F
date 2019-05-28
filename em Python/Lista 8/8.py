a = input('Frase:\n').split(' ')
b = input('Palavra a ser trocada:\n')
c = input('Palavra nova:\n')
final = []
for i in a:
    if i == b:
        final.append(c)
    else:
        final.append(i)
print('Produto Final:\n')
for i in range(len(final)):
    print(final[i], end=' ')
