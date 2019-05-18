x = [[float(input()) for j in range(4)] for i in range(12)]
somam = [0 for k in range(12)]
somaa = 0
for i in range(12):
    for j in range(4):
        somam[i] += x[i][j]
        print("Total vendido na semana %d: R$ %.2f" % (j+1, x[i][j]))
    print("Total vendido no Mes %d: R$ %.2f" % (i+1, somam[i]))
    somaa += somam[i]
print("Total vendido no ano: R$ %.2f" % somaa)