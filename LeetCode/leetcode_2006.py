from collections import defaultdict
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        result = 0
        hash_table = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] - k in hash_table:
                result += hash_table[nums[i] - k]
            if nums[i] + k in hash_table:
                result += hash_table[nums[i] + k]
            hash_table[nums[i]] += 1
        return result