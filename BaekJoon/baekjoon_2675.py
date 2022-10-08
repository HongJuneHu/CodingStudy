import sys
a = int(sys.stdin.readline())
for i in range(a):
    b, c = sys.stdin.readline().strip().split()
    for j in c:
        print(j*int(b), end='')
    print()