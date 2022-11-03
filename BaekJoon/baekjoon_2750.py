import sys

input = sys.stdin.readline

cnt = int(input())

res = []

for i in range(cnt):
    res.append(int(input()))

res.sort()

for i in range(cnt):
    print(res[i])