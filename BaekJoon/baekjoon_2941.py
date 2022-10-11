import sys

def cntset(res, cnt):
    return res+1, cnt+2

def readstr(a, cnt):
    return a[cnt]+a[cnt+1]
a = sys.stdin.readline().strip()
#a = input()
cnt = 0
res = 0
while cnt < len(a):
    if cnt+2 < len(a):
        if a[cnt] + a[cnt+1] + a[cnt+2] == 'dz=':
            res, cnt = cntset(res, cnt+1)
            continue
    if cnt+1 < len(a):
        if readstr(a, cnt) == 'c=':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 'c-':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 'd-':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 'lj':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 'nj':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 's=':
            res, cnt = cntset(res, cnt)
            continue
        elif readstr(a, cnt) == 'z=':
            res, cnt = cntset(res, cnt)
            continue
        else:
            cnt += 1
            res += 1
    else:
        cnt += 1
        res += 1
    
    
print(res)