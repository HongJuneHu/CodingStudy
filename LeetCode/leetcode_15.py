class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            (j, k) = (i + 1, len(nums) - 1)

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    result.append((nums[i], nums[j], nums[k]))
                    k -= 1
                    while j < k and nums[k] \
                        == nums[k + 1]:
                        k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
                    
        return result