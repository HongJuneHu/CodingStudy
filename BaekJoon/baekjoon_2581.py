import sys
import math

check = [True] * 10001
check[0], check[1] = False, False
res = []
for i in range(2, int(math.sqrt(10000))+1):
    if check[i]:
        res.append(i)
        j = 2
        while i * j <= 10000:
            check[i * j] = False
            j += 1

res = [x for x in range(10001) if check[x]]

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

#a = int(input())
#b = int(input())

s = 0
first = True

for i in range(a, b+1):
    if check[i]:
        s += i
        if first:
            f = i
            first = False
if s == 0:
    print(-1)
else:
    print(s)
    print(f)