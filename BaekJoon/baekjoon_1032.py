a = int(input())
b = []
for i in range(a):
    b.append(input())
if len(b) == 1:
    print(b[0])
c = b[0]
cnt = 1
if len(b) != 1:
    while(cnt < len(b)):
        for i in range(len(b[0])):
            if c[i] != b[cnt][i]:
                c = c[:i] + '?' + c[i+1:]
        cnt += 1
    print(c)