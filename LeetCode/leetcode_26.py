class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # return the nums after modification, with unique nums length
        k = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i + 1]
                k += 1
        return k