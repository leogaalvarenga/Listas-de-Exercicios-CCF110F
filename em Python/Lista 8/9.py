dnain = input('Insira a cadeia de DNA:\n')
dnain.upper()
dnaout = ''
for i in dnain:
    if i == 'A':
        dnaout += 'T'
    elif i == 'T':
        dnaout += 'A'
    elif i == 'C':
        dnaout += 'G'
    elif i == 'G':
        dnaout += 'C'
print('Cadeia complementar:\n%s'%dnaout)
