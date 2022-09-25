a = {1: 0,
     2: 0,
     3: 0,
     4: 0,
     5: 0,
     6: 0}

b = list(map(int, input().split()))

for i, v in enumerate(b):
    a[v] += 1

c = max(a, key=a.get)

if a[c] == 3:
    print(10000+c*1000)
elif a[c] == 2:
    print(1000+c*100)
else:
    print(max(b)*100)