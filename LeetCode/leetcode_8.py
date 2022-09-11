class Solution:
    def myAtoi(self, s: str) -> int:
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        cnt = 0
        res = ""
        sign = 0
        start = 0
        while True:
            if len(s) == cnt:
                break
            elif start == 1 and s[cnt] not in num:
                break
            elif s[cnt] == " ":
                cnt += 1
                continue
            elif s[cnt] in num or s[cnt] == '+':
                res += s[cnt]
                start = 1
            elif s[cnt] == '-':
                sign = 1
                start = 1
            else:
                break
            cnt += 1
        try:
            res = int(res)
            if sign:
                res *= -1
        except ValueError:
            res = 0
        if res > 2**31 -1:
            return 2**31-1
        elif res < -2**31:
            return -2**31
        
        return res