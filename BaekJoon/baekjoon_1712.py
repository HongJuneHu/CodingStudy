import sys

A = list(map(int, sys.stdin.readline().split()))

try:
    res = A[0]//(A[2]-A[1])+1
except ZeroDivisionError:
    res = -1

if A[1] > A[2]:
    res = -1

print(res)