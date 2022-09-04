cnt = 0
while True:
    a = input()
    a = a.lower()
    if a == '#':
        break
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
            cnt += 1
    print(cnt)
    cnt = 0
            