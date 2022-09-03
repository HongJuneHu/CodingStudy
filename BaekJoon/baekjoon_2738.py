a = input().split()
a = list(map(int, a))
b = []

for i in range(a[0]*2):
    b.append(input())

c = []

for i in range(len(b)):
    b[i] = b[i].split()
    
for i in range(len(b)):
    c.append(list(map(int, b[i])))
    
for i in range(a[0]):
    for j in range(a[1]):
        print(c[i][j] + c[i+a[0]][j], end=' ')
    print()