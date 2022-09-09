class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            res = self.check(s, i, i)
            if len(res) > len(result):
                result = res
            res = self.check(s, i, i+1)
            if len(res) > len(result):
                result = res
        return result
            
            
    def check(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1 : j]