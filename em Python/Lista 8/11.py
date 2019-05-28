a = input('Frase:\n')
saida = ''
for i in a:
    if i == ' ':
        saida += '#'
        continue
    saida += i
print(saida)
