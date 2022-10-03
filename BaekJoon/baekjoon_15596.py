import sys

def solve(a):
    ans = sum(a)
    return ans
a = list(map(int, sys.stdin.readline().split()))
print(sum(a))