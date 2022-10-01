import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = max(b)
s = 0
for i in range(a):
    s += b[i]/c*100
s /= a
print(s)