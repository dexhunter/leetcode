class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev, o = 0, x
        while x:
            rev = x%10+rev*10
            x = (int)(x/10)
        return rev == o
