res = set()
base = set(range(1, 10001))
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    res.add(i)
        
res = sorted(base - res)
for i in res:
    print(i)