import sys

def res(n):
    if n < 3:
        return -1
    elif n % 5 == 0:
        return n // 5
    elif (n - 3) % 5 == 0:
        return n // 5 + 1
    elif n < 6:
        return -1
    elif (n - 6) % 5 == 0:
        return (n - 6) // 5 + 2
    elif n < 9:
        return -1
    elif (n - 9) % 5 == 0:
        return (n - 9) // 5 + 3
    elif n < 12:
        return -1
    elif (n - 12) % 5 == 0:
        return (n - 12) // 5 + 4
    elif n % 3 == 0:
        return n // 3
    else:
        return -1

#a = int(sys.stdin.readline())
a = int(input())

print(res(a))