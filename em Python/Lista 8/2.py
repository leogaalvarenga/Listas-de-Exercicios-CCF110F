import random
a=[]
b=[]
c=0
temp=[]
for i in range(10):
    a.append(random.randint(1, 6))
print(a)
for i in range(10):
    c = a[i]
    if c not in temp:
        temp.append(c)
        b.append(a.count(c))
print(b)
