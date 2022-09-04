a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_s = 0
b_s = 0
a_s = a[0] * 6 + a[1] * 3 + a[2] * 2 + a[3] + a[4] * 2
b_s = b[0] * 6 + b[1] * 3 + b[2] * 2 + b[3] + b[4] * 2

print(str(a_s) + " " + str(b_s))