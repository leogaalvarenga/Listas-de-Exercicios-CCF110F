lista = [['Vectra', 9], ['Gol', 10], ['Corsa', 11], ['Fit', 12.5]]
b = [[0 for j in range(2)] for i in range(4)]
m=[]
for i in range(4):
    b[i][0] = lista[i][0]
    b[i][1] = (1000 / lista[i][1]) * 3.5
    m.append(lista[i][1])
print("%s: %d km/l"%(b[m.index(max(m))][0], lista[m.index(max(m))][1]))
print('----------------')
for i in range(4):
    print('%s:'%b[i][0], end=' ')
    print('R$ %.2f'%b[i][1])
