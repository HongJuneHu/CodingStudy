import math
a = input().split()
a = list(map(int, a))
a.sort()
b = []

def prime(x):
    for i in range(2, x + 1):
        p = True
        for j in range(2, i + 1):
            if i == 2:
                break
            if i > j and i % j == 0:
                p = False
                break
            else:
                continue
        if p:
            b.append(i)

for i in range(5):
    for j in range(2, a[i]):
        if a[i] % j == 0:
            b.append(j)
