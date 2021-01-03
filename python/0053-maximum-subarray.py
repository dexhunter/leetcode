class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)

class Failed_Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] >= 0 and nums[1] >= 0:
                return nums[0] + nums[1]
            elif nums[0] >= 0:
                return nums[0]
            elif nums[1] >= nums[0]:
                return nums[1]
            elif nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]
        l = 0 # start of sum # left
        r = None # right
        s_max = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[l] and nums[i] >= 0:
                l = i
            elif nums[l] + nums[i] < 0:
                r = i
            print(l,r)
            # print(nums[l])
            s = sum(nums[l:r])
            if s > s_max:
                s_max = s
        return s_max
                
        