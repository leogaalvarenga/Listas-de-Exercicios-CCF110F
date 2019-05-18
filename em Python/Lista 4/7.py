a1, an = input("Insira o primeiro e último termos da PA:\n").split(" ")
a1 = int(a1)
an = int(an)
n = int(input("Insira o numero de termos existentes nessa PA: \n"))
S = ((a1 + an)*n)/2
print(S)