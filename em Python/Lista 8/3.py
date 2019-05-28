def pegar_prox(num, lista):
    return min(lista, key=lambda x:abs(x-num))


n = int(input('Tamanho do vetor:\n'))
vetor = [float(input('Termo na posição %d:\n'%i)) for i in range(n)]
soma = 0
for i in range(len(vetor)):
    soma += vetor[i]
soma /= len(vetor)
print(soma)
print(pegar_prox(soma, vetor))
