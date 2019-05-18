# x = []
# n = [0 for i in range(15)]
# for i in range(15):
#     a = int(input())
#     x.append(a)
# for j in x:
#     n[14] = max(x)
#     n[0] = min(x)
a = []
for i in range(15):
    n = int(input())
    a.append(n)
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
print(a)

# basicamente a funcao sorted() nativa do Python