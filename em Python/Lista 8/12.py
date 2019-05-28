# def reverter(string):
#     final = ''
#     for i in range(0, len(string), -1):
#         final += string[i]
#     return final
#

sa = input('Frase 1:\n')
sb = input('Frase 2:\n')
teste = True
temp = sb[::-1]
cont = len(sa)-1
while teste:
    for i in range(len(sa)-1):
        if sa[i] != temp[i]:
            teste = False
            print('Não são Palíndromas mútuas.')
    temp = sa[::-1]
    for i in range(len(sb)-1):
        if sb[i] != temp[i]:
            teste = False
            print('Não são Palíndromas mútuas.')
    if teste:
        print('Palíndromas Mútuas.')
        break

#     for i in sa:
#         if i != temp[cont]
#             print('Não são Palíndromas mútuas.')
#             teste = False
#         cont += 1
#     temp = reverter(sa)
#     for i in range(len(sb)):
#         if sb[i] != temp[i]:
#             print('Não são Palíndromas mútuas.')
#             teste = False
