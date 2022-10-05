import sys

a = int(sys.stdin.readline())
b = 0

for i in range(1, a+1):
    numlist = list(map(int, str(i)))
    
    if i < 100:
        b += 1
    elif numlist[0]-numlist[1] == numlist[1]-numlist[2]:
        b += 1
print(b)