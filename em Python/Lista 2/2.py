nbola = int(input("Insira o numero da bola sorteada: \n"))
valor = float(input("Insira o valor do dinheiro restante da caixa: \n"))

if nbola == 0:
    print("O premio recebido foi de", 0.05 * valor, "reais.")

elif nbola == 1:
    print("O premio recebido foi de", 0.25 * valor, "reais.")

elif nbola == 2:
    print("O premio recebido foi de", 0.10 * valor, "reais.")

elif nbola == 3:
    print("O premio recebido foi de", 0.07 * valor, "reais")

elif nbola == 4:
    print("O premio recebido foi de", 0.08 * valor, "reais")

elif nbola == 5:
    print("O premio recebido foi de", 0.05 * valor, "reais")

elif nbola == 6:
    print("O premio recebido foi de", 0.15 * valor, "reais")

elif nbola == 7:
    print("O premio recebido foi de", 0.12 * valor, "reais")

elif nbola == 8:
    print("O premio recebido foi de", 0.03 * valor, "reais")

elif nbola == 9:
    print("O premio recebido foi de", 0.10 * valor, "reais")

else:
    print("Numero inserido invalido, tente novamente.")