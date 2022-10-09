import sys

a = list(map(str, sys.stdin.readline().split()))

b = int(a[0][2])*100 + int(a[0][1]) * 10 + int(a[0][0])
c = int(a[1][2])*100 + int(a[1][1]) * 10 + int(a[1][0])

print(max(b, c))