import sys
import math

a, b = map(int, input().split())


check = [True] * 1000001
check[0], check[1] = False, False
res = []

for i in range(2, int(math.sqrt(1000000))+1):
    if check[i]:
        res.append(i)
        j = 2
        while i * j <= 1000000:
            check[i * j] = False
            j += 1

res = [x for x in range(1000001) if check[x]]

i = 0

while True:
    if res[i] <= b and res[i] >= a:
        print(res[i])
    elif res[i] > b:
        break
    i += 1