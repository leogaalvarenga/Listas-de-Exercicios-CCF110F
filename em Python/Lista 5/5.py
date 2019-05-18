maior = 1
maior2 = 0
for i in range(10):
    n = int(input())
    if n > maior:
        maior2 = maior
        maior = n
    if n == maior:
        maior2 = n
    if n > maior2 and n < maior:
        maior2 = n
print(maior)
print(maior2)