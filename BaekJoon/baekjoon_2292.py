import sys

a = int(sys.stdin.readline())

b = 1
res = 1

while a > b:
    b += res*6
    res += 1
print(res)