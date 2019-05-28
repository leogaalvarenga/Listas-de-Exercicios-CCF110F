meses = {'01' : 'de janeiro de', '02' : 'de fevereiro de', '03' : 'de março de', '04' :'de abril de',
        '05' :' de maio de', '06' : 'de junho de', '07' : 'de julho de', '08' : 'de agosto de', '09' : 'de setembro de',
        '10' : 'de outubro de', '11' : 'de novembro de', '12' : 'de dezembro de' }
data = input().split('/')
saida = ''
for i in data:
    if i in meses:
        saida += (' ' + meses[i] + ' ')
    else:
        saida += i
print(saida)
