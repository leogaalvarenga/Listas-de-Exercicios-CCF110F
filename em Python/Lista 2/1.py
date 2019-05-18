idade = int(input("Insira a idade do paciente, em anos: \n"))
peso = float(input("Insira o peso do paciente, em quilogramas: \n"))

if idade >= 12 and peso >= 60:
    print("O paciente deve tomar 40 gotas do medicamento.")

elif idade >= 12 and peso < 60:
    print("O paciente deve tomar 35 gotas do medicamento.")

elif idade < 12 and 5 <= peso <= 9:
    print("O paciente deve tomar 5 gotas do medicamento.")

elif idade < 12 and 9 <= peso <= 16:
    print("O paciente deve tomar 10 gotas do medicamento.")

elif idade < 12 and 16 <= peso <= 24:
    print("O paciente deve tomar 11 gotas do medicamento.")

elif idade < 12 and 24 <= peso <= 30:
    print("O paciente deve tomar 20 gotas do medicamento.")

elif idade < 12 and peso > 30:
    print("O paciente deve tomar 30 gotas do medicamento.")

