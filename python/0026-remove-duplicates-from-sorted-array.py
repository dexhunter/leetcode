class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        current = nums[0]
        for i in nums[1:]:
            if current == i:
                nums.remove(i)
            else:
                current = i
        return len(nums)

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
