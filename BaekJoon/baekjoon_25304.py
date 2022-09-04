a = int(input())
b = int(input())
r = 0
for i in range(b):
    c, d = list(map(int, input().split()))
    r += c * d
if r == a:
    print("Yes")
else:
    print("No")