class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for ind, i in enumerate(nums):
            if i == target:
                return ind
            elif i > target:
                return ind
        return len(nums)

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
