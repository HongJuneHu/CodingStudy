class Solution:
    def romanToInt(self, s: str) -> int:
        calc = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }
        res = 0
        for i in range(len(s)):
            try:
                if calc[s[i]] < calc[s[i+1]]:
                    res -= calc[s[i]]
                else:
                    res += calc[s[i]]
            except IndexError:
                res += calc[s[i]]
        return res