import sys

a = int(sys.stdin.readline())
#a = int(input())

res = [[0 for i in range(15)] for i in range(15)]

for i in range(1, 15):
    res[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        if j == 1:
            res[i][j] = 1
        else:
            res[i][j] = res[i-1][j] + res[i][j-1]

for i in range(a):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    #k = int(input())
    #n = int(input())
    print(res[k][n])