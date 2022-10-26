class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - i - 1)
        
        num += 1
        res = []
        
        for i in range(len(str(num))):
            res.append(str(num)[i])
        return res