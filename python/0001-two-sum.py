class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# the above solution is no longer accepted

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for ind, n in enumerate(nums):
            if target-n in res:
                return [res[target-n], ind]
            else:
                res[n] = ind
