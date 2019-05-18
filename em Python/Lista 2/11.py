import sys

n = 0
for i in range(sys.maxsize**10):
    n = float(input("Insira um numero: \n"))
    if n == -999:
        break
    else:
        m = n * 3
        print(m)
