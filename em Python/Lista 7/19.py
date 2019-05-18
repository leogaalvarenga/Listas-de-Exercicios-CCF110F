n = [[float(input()) for j in range(2)] for i in range(5)]
for i in range(5):
    print("Delegaçao %d\nAltura maxima: %.2f" % (i+1, max(n[i])))