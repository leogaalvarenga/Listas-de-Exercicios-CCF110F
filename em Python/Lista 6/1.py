n = 0
p = 0
x =[0 for i in range(6)]
for i in range(6):
    x[i] = int(input())
    if x[i] > 0:
        p += 1
    elif x[i] < 0:
        n += 1
if x in [0]:
    print("Nenhum valor positivo ou negativo foi inserido.\n")
else:
    print("%d numeros positivos inseridos e % numeros negativos inseridos\n"%(p, n))