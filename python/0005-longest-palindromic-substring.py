class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(st: str) -> bool:
            if (st == st[::-1]):
                return True
            else:
                return False
        longest = ""
        longest_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                st = s[i:j]
                if isPalindrome(st) and len(st) > longest_len:
                    longest = st
                    longest_len = len(st)
        return longest
