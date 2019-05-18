f = 0
m = 0
s = 0
n = 0
fr = 0
mn = 0
for i in range(2000):
    sexo = int(input())
    resp = int(input())
    if resp == 1:
        sexo += 1
        if sexo == 1:
            mn += 1
    elif resp == 2:
        n += 1
        if sexo == 2:
            fr += 1
    if sexo == 1:
        m += 1
    else:
        f += 1
print("Pessoas que disseram sim:", s)
print("Pessoas que disseram sim:", n)
print("Mulheres que disseram sim (%)", ((fr * 100)/f))
print("Homens que disseram nao (%)", ((mn *100)/f))