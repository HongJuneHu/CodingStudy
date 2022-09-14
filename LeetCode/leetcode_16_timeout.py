class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 100000
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums)-1
            
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return tmp
                elif abs(res - target) > abs(tmp - target):
                    res = tmp
                elif tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
        return res