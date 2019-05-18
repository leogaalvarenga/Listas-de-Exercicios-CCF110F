n = 1
d = 1
v = 0
for i in range(100):
    v += n/d
    n += 2
    if d < 50:
        d += 1
    else:
        continue
print(v)