a = int(input())
b = int(input())

s1 = a * (b % 10)
s2 = a * (b // 10 % 10)
s3 = a * (b // 100)

print(s1)
print(s2)
print(s3)
print(s1 + s2*10 + s3*100)