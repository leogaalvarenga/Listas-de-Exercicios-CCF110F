n = int(input("Insira um numero qualquer: \n"))

if n > 0:
    if n % 10 == 0:
        print("o numero inserido pode ser dividido por 10.")
    if n % 5 == 0:
        print("o numero inserido pode ser dividido por 5.")
    if n % 2 == 0:
        print("o numero inserido pode ser dividido por 2.")
else:
    print("Erro")