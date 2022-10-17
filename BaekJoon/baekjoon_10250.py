import sys

a = int(input()) #int(sys.stdin.readline())

for i in range(a):
    #b = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, input().split()))
    
    floor = b[2] % b[0]
    number = b[2] // b[0] +1
    if floor == 0:
        floor = b[0]
        number = b[2] // b[0]
    print(floor*100+number)