while True:
    try:
        a = input().split()
        a = list(map(int, a))
        print(a[1]//(a[0]+1))
    except EOFError:
        break