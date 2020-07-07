class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_indices = {}
        cursor = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in current_indices:
                cursor = max(current_indices[s[i]], cursor)
            ans = max(ans, i - cursor +1)
            current_indices[s[i]] = i + 1
        return ans
