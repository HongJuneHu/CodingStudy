import sys
checker = {
    'a': False,
    'b': False,
    'c': False,
    'd': False,
    'e': False,
    'f': False,
    'g': False,
    'h': False,
    'i': False,
    'j': False,
    'k': False,
    'l': False,
    'm': False,
    'n': False,
    'o': False,
    'p': False,
    'q': False,
    'r': False,
    's': False,
    't': False,
    'u': False,
    'v': False,
    'w': False,
    'x': False,
    'y': False,
    'z': False
    }

a = int(sys.stdin.readline())

checkbreak = False
res = 0
for i in range(a):
    checker_temp = checker.copy()
    b = sys.stdin.readline().strip()
    tmp = b[0]
    for j in b:
        if checker_temp[j]:
            checkbreak = True
            break
        if tmp != j:
            checker_temp[tmp] = True
        tmp = j
    if not(checkbreak):
        res += 1
    checkbreak = False
print(res)