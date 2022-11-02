import sys

input = sys.stdin.readline
M, x, y = -1, 0, 0
for i in range(9):
    a = list(map(int, input().split()))
    for j in range(9):
        if M < a[j]:
            M, x, y = a[j], i+1, j+1

print(M, x, y, sep="\n")