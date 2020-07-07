class Solution:
    def countAndSay(self, n: int) -> str:
        import itertools
        s = "1"
        for _ in range(n-1):
            s = ''.join(str(len(list(ctr)))+ch for ch, ctr in itertools.groupby(s))
        return s
