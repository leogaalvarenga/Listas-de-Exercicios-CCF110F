numn = int(input("Insira seu numero: \n"))

if numn not in [1, 2, 3, 4, 5, 6, 7]:
    print("Dia da semana invalido.")
elif numn == 1:
    print("Domingo")
elif numn == 2:
    print("Segunda-feira")
elif numn == 3:
    print("Terça-feira")
elif numn == 4:
    print("Quarta-feira")
elif numn == 5:
    print("Quinta-feira")
elif numn == 6:
    print("Sexta-feira")
else:
    print("Sábado")
