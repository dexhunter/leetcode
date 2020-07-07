class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        from statistics import median
        return median(nums1 + nums2)
