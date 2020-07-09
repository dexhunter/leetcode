class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            for i in nums:
                if i == val:
                    nums.remove(i)
        return len(nums)

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count += 1
        return count

class Solution3:
  def removeElement(self, nums, val):
    start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1
        else:
            start +=1
    return start
