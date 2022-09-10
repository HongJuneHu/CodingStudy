class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        tmp = []
        size = -1
        if x < 0:
            sign = 1
            x *= -1
        else:
            sign = 0
        while x != 0:
            tmp.append(x % 10)
            x = x // 10
            size += 1
        for i in range(len(tmp)):
            res += tmp[i] * 10 ** size
            size -= 1
        if sign:
            res *= -1
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res