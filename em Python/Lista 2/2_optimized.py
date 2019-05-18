nbola = int(input("Insira o numero da bola sorteada: \n"))
valor = float(input("Insira o valor do dinheiro restante da caixa: \n"))

dict = {'b0': 0.05 * valor, 'b1': 0.25 * valor, 'b2': 0.10 * valor,
        'b3': 0.07 * valor, 'b4': 0.08 * valor,
        'b5': 0.05 * valor, 'b6': 0.15 * valor,
        'b7': 0.12 * valor, 'b8': 0.03 * valor,
        'b9': 0.10 * valor}

if nbola in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if nbola == 0:
        print("O premio recebido foi de {} reais." .format(dict['b0']))
    if nbola == 1:
        print("O premio recebido foi de {} reais.".format(dict['b1']))
    if nbola == 2:
        print("O premio recebido foi de {} reais.".format(dict['b2']))
    if nbola == 3:
        print("O premio recebido foi de {} reais.".format(dict['b3']))
    if nbola == 4:
        print("O premio recebido foi de {} reais.".format(dict['b4']))
    if nbola == 5:
        print("O premio recebido foi de {} reais.".format(dict['b5']))
    if nbola == 6:
        print("O premio recebido foi de {} reais.".format(dict['b6']))
    if nbola == 7:
        print("O premio recebido foi de {} reais.".format(dict['b7']))
    if nbola == 8:
        print("O premio recebido foi de {} reais.".format(dict['b8']))
    if nbola == 9:
        print("O premio recebido foi de {} reais.".format(dict['b9']))
else:
    print("Numero inserido invalido, tente novamente.\n")