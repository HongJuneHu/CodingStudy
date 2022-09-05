class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, value in enumerate(nums):
            tma = target - nums[i]
            nums[i] = None
            if tma in nums:
                return [i, nums.index(tma)]