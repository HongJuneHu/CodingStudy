a = input().split()
a = list(map(int, a))

b = []
b.append(a[0])
b.append(a[1])
b.append(a[2] - a[0])
b.append(a[3] - a[1])
b.sort()
print(b[0])