class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s.startswith('-'):
            s = s[1:]
            s += '-'
        i = int(s[::-1])
        if i>2**31-1 or i<-2**31:
            return 0
        return i
