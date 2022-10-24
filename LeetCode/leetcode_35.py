class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            res = nums.index(target)
        except ValueError:
            nums.insert(0, target)
            nums.sort()
            res = nums.index(target)
        return res
    
"""
start = 0
end = length - 1

while start <= end:
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

return start
"""