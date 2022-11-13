import sys

input = sys.stdin.readline

a, b = map(int, input().split())

c = list(map(int, input().split()))
lc = len(c)
ans = 0

for i in range(lc):
    for j in range(i+1, lc):
        for k in range(j+1, lc):
            if b >= c[i]+c[j]+c[k]:
                if abs(b - ans) > abs(b - (c[i]+c[j]+c[k])):
                    ans = c[i] + c[j] + c[k]
                
                
print(ans)