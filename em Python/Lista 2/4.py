numn = int(input("Insira seu numero: \n"))

if numn not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    print("Mês invalido.")
elif numn in [1, 2, 3]:
    print("Primeiro Trimestre")
elif numn in [4, 5, 6]:
    print("Segundo Trimestre")
elif numn in [7, 8, 9]:
    print("Terceiro Trimestre")
else:
    print("Quarto Trimestre")
