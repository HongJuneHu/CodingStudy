a = int(input())

c0 = [1, 0, 1]
c1 = [0, 1, 1]


def fib(n):
    length = len(c0)
    if n >= length:
        for i in range(length, n+1):
            c0.append(c0[i-1] + c0[i-2])
            c1.append(c1[i-1] + c1[i-2])
    print(c0[n], c1[n])

for i in range(a):
    fib(int(input()))