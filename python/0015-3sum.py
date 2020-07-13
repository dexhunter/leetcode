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

class Solution3(object):
    def threeSum(self, nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	# timsort: O(nlogn)
	nums.sort()

	# Stored val: Really fast
	n = len(nums)

	# Hash table
	solutions = set()

	# O(n): hash tables are really fast :)
	unique_set = set(nums)
	# covers a lot of edge cases with 2 memory lookups and 1 hash so it's worth the time
	if len(unique_set) == 1 and 0 in unique_set and len(nums) > 2:
	    return [[0, 0, 0]]

	# O(n) but a little faster than enumerate.
	i = 0
	while i < n - 2:
	    num = nums[i]

	    left = i + 1
	    right = n - 1

	    # O(1/2k) where k is n-i? Not 100% sure about this one
	    while left < right:
		# I think its worth the memory alloc for the vars to not have to hit the list index twice. Not sure
		# how much faster it really is. Might save two lookups per cycle.
		left_num = nums[left]
		right_num = nums[right]
		s = num + left_num + right_num  # check if current sum is 0
		if s == 0:
		    # add to the solution set only if this triplet is unique
		    # Hash lookup
		    solutions.add(tuple([right_num, num, left_num]))
		    right -= 1
		    left += 1
		elif s > 0:
		    right -= 1
		else:
		    left += 1
	    i += 1

	return list(solutions)
