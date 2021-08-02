class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ind = [False]*len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (ind[i-len(word)] or i-len(word)==-1):
                    ind[i] = True
            
        return ind[-1]