class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(nums, [], results)
        return results


    def dfs(self, nums, path, res):
        if len(nums)<1:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

