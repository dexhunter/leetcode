class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        prev_ch = 1e5
        for ch in s:
            sum += d[ch]
            if prev_ch < d[ch]:
                sum -= 2*prev_ch
            prev_ch = d[ch]
        return sum

class Solution2:
    "another one found on discussion, which I think is more pythonic"
    def romanToInt(self, s):
	d={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
	res, p = 0, 'I'
	for c in s[::-1]:
	    res, p = res - d[c] if d[c] < d[p] else res + d[c], c
	return res
