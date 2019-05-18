dias = int(input(" Insira sua idade, em dias: \n"))
anos = dias // 365
meses = dias - (anos * 365)
print("Sua idade é de %s anos, %s meses e " %(anos, meses))