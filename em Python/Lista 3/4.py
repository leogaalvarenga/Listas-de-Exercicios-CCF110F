anos = int(input("Você deverá inserir sua idade em anos, meses e dias, respectivamente: \n"))
meses = int(input())
dias = int(input())

anos *= 365
meses *= 30
idade = anos + meses + dias

print("Sua idade, em dias, é de {}.".format(idade))