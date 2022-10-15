import sys

a = int(sys.stdin.readline())
l = 1

while a > l:
    a -= l
    l += 1

if l % 2 == 0:
    print(a, '/', l-a+1, sep='')
else:
    print(l-a+1, '/', a, sep='')