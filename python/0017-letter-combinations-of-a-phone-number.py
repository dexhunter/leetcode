class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keymapping = {'2':'abc', '3': 'def', '4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        combinations = [''] if digits else []
        for i in digits:
            combinations = [p + q for p in combinations for q in keymapping[i]]
        return combinations

