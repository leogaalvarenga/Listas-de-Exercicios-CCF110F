s1 = input('')
s2 = input('')
teste = True
while teste:
    lista1 = sorted(s1.upper())
    lista2 = sorted(s2.upper())
    for i in lista1:
        if lista2.index(i) != lista1.index(i) or i not in lista2:
            teste = False
    print('É um anagrama.')
    break
