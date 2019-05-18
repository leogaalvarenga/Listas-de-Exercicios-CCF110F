qtd = []
p = []
id = []
for i in range(100):
    preco = float(input())
    p.append(preco)
    x = int(input())
    id.append(x)
    q = int(input())
    qtd.append(q)
print(" Produto | Faturamento Mensal")
for i in range(100):
    print(" %d | R$ %.2f" %(id[i], (p[i] * qtd[i])))