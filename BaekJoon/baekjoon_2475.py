a = input().split()
a = list(map(int, a))
b = 0
for i in range(5):
    b += a[i]**2

print(b % 10)