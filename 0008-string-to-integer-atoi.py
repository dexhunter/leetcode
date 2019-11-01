class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        s = s.strip()
        if len(s) < 2:
            if s.isdigit():
                return int(s)
            return 0
        if s[0].isdigit() or s[0] == '-' or s[0] =='+':
            sign = -1 if s.startswith('-') else 1
            if not s[0].isdigit() and not s[1].isdigit() and s[1] != '.':
                return 0
            x = sign * int(re.search(r'\d+', s).group())

            if x < - 2**31:
                return -2**31
            elif x > 2**31-1:
                return 2**31-1
            else:
                return x
        return 0


class Solution2:
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('^[+\-]?\d+', str)

        try:
            res = int(''.join(str))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN:
                return MIN
            return res
        except:
            return 0
