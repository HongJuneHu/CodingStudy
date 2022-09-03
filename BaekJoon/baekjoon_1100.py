# 00 02 04 06
# 11 13 15 17
a = []
cnt = 0
for i in range(8):
    a.append(input())

for i in range(8):
    for j in range(8):
        if i % 2 == 1:
            if j % 2 == 1:
                if a[i][j] == 'F':
                    cnt += 1
        if i % 2 == 0:
            if j % 2 == 0:
                if a[i][j] == 'F':
                    cnt += 1
print(cnt)