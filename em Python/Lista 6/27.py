e1 = 800
e2 = 900
e3 = 1000
t = []
id = []
while True:
    try:
        i = int(input())
        id.append(i)
        tt = int(input())
        t.append(tt)
    except EOFError:
        break
for i in t:
    if e1 > t[i] < e2 and t[i] < e3:
        e1 = t[i]
        e2 = e3 = e1
    if e3 > t[i] > e2 and t[i] > e1:
        e3 = t[i]
    if e2 > t[i] < e3 and t[i] > e1:
        e2 = t[i]
    if e1 > t[i] < e2:
        e1 = t[i]