maior = 0
menor = 100
pa = 0
pe = 0
n = int(input())
if n <= 50:
    x = [0 for i in range(n)]
    for i in range(n):
        x[i] = int(input())
        if x[i] > maior:
           maior = x[i]
           pa = i
        if x[i] < menor:
            menor = x[i]
            pe = i
    print("Maior = %d\nSua posiçao = %d\nMenor = %d\nSua posiçao = $d" %(maior, pa, menor, pe))