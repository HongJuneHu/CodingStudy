import sys

input = sys.stdin.readline

a, b = map(int, input().split())

c = list(map(int, input().split()))

c.sort()

print(c[-b])
