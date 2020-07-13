class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if len(nums) < 3:
            return sol

        nums.sort()
        for ind, n in enumerate(nums[:-2]):

            left, right = ind+1, len(nums)-1

            while left < right:
                s = [n,nums[left],nums[right]]
                if sum(s) == 0:
                    if s not in sol:
                        sol.append(s)
                    left += 1
                    right -= 1
                elif sum(s) > 0:
                    right -= 1
                else:
                    left += 1
        return sol

# The above solution is no longer accepted (time out) due to `not in` operation

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if len(nums) < 3:
            return sol

        nums.sort()
        for ind in range(len(nums)-2):

            if ind > 0 and nums[ind] == nums[ind-1]: continue

            left, right = ind+1, len(nums)-1

            while left < right:
                tot = nums[ind] + nums[left] + nums[right]
                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    sol.append([nums[ind], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return sol

