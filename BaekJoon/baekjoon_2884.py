H, M = map(int, input().split())

if M - 45 < 0:
    if H-1 < 0:
        print("23 " + str(60+M-45))
    else:
        print(str(H-1), str(60+M-45))
else:
    if H - 1 < 0:
        print(str(H), str(M-45))
    else:
        print(str(H), str(M-45))