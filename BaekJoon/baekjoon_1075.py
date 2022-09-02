a = int(input())
a = a - (a % 100)
b = int(input())
while(a % b != 0):
    a += 1

if a % 100 < 10:
    print("0"+str((a % 100)))
else:
    print(a % 100)