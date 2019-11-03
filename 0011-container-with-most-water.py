class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        for w in range(len(height)-1, 0, -1):
            if height[l] >= height[r]:
                res = max(res, height[r]*w)
                r -= 1
            else:
                res = max(res, height[l]*w)
                l += 1
        return res
