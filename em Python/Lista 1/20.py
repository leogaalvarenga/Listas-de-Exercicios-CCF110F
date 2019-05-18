idade = int(input("Insira sua idade: \n"))

if idade < 16:
    print("Voce não possui deveres eleitorais.")

elif idade < 18:
    print("Voce é um eleitor facultativo, isto é, pode votar mas ainda não é obrigado a fazê-lo.")

elif idade >= 18 and idade < 65:
    print("Você é obrigado por lei a votar, fique em dia com seus deveres eleitorais!")

