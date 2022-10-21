import sys

#a = int(input())
a = int(sys.stdin.readline())
b = 2

while a != 1:
    if a % b == 0:
        print(b)
        a //= b
    else:
        b += 1