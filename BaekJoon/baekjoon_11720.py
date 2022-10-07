import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()
res = 0
for i in b:
    res += int(i)
print(res)