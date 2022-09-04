a = [True for i in range(30)]
for i in range(28):
    a[int(input())-1] = False
    
for i in range(30):
    if a[i] == True:
        print(i+1)