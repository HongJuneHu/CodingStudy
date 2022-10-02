import sys
a = int(sys.stdin.readline())
s = 0
cnt = 0
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    s = sum(b) - b[0]
    s /= b[0]
    for j in range(b[0]):
        if b[j+1] > s:
            cnt += 1
    result = round(cnt/b[0]*100, 3)
    print('{:.3f}%'.format(result))
    cnt = 0