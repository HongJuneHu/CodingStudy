import sys
a = set()
for i in range(10):
    b = int(sys.stdin.readline())
    a.add(b%42)
print(len(a))