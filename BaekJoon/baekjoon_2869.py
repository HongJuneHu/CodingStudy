import sys
import math

a = list(map(int, sys.stdin.readline().split()))

res = math.ceil((a[2]-a[0]) / (a[0]-a[1])) + 1
print(res)