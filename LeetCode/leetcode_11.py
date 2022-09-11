class Solution:
    def maxArea(self, height: List[int]) -> int:
        result, i, j = 0, 0, len(height)-1
        while i < j:
            if height[i] > height[j]:
                res = height[j] * (j - i)
                j -= 1
            else:
                res = height[i] * (j - i)
                i += 1
            if res > result:
                result = res
        return result