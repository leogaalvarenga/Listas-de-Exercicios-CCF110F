n = int(input("Numero de eleitores:\n"))
c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0

for i in range(n):
    voto = int(input("Insira seu vot: \n"))
    if voto == 1:
        c1+=1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        c4 += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
print("Total de votos por candidato: \n 1 = %s \n 2 = %s \n 3 = %s \n 4 = %s", (c1, c2, c3, c4))
print("Votos em branco: ", branco)
print("Votos nulos: ", nulo)
print("Percetual de votos brancos e nulos sobre o total:", ((nulo+branco)*100 / n))