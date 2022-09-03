a = input()
if int(a) < 10:
    a = '0'+a
b = int(a)
cnt = 0
while True:
    b = ((b // 10) + (b % 10)) % 10 + (b % 10 * 10)
    cnt += 1
    if b == int(a):
        break
print(cnt)