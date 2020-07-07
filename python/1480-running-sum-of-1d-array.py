class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for ind, i in enumerate(nums):
            res.append(sum(nums[:ind+1]))
        return res

class Solution(object):
    def runningSum(self, nums):
        return [sum(nums[:i+1]) for i in range(len(nums))]
