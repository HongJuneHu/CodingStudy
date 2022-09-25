a, b = map(int, input().split())
c = int(input())
cnt = 0

b += c
cnt = b // 60
b %= 60
a += cnt
a %= 24
print(str(a), str(b))