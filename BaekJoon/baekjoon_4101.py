while True:
    a = input().split()
    a = list(map(int, a))
    if a[0] == 0 and a[1] == 0:
        break
    elif a[0] > a[1]:
        print("Yes")
    elif a[0] <= a[1]:
        print("No")