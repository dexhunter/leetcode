class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])+1):
            prefix = strs[0][:i]
            for s in strs:
                if not s.startswith(prefix):
                    return prefix[:-1]
        return prefix

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_s = min(strs)
        max_s = max(strs)

        for i, ch in enumerate(min_s):
            if ch != max_s[i]:
                return min_s[:i]
        return min_s
