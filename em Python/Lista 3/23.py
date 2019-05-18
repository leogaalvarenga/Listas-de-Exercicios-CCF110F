print("1 \n1")
soma = 2
temp = 2
ant = 1
for i in range(18):
    soma+=ant
    ant=temp
    temp = soma
    print(soma)