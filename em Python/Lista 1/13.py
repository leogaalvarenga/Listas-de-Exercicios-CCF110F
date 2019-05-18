dividendo = float(input("Insira um dividendo: \n"))
divisor = float(input("Insira um divisor: \n"))

if divisor == 0:
    print("Divisão não permitida; seu divisor é zero.")

else:
    quo = dividendo / divisor
    resto = dividendo % divisor
    print("O resultado de seu divisão foi", quo, "e seu resto foi ", resto)
