class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            prev = self.generate(numRows-1)
            last = prev[-1]
            temp = [1]
            for i in range(len(last)-1):
                temp = temp + [last[i]+last[i+1]]
            temp = temp + [1]
            return prev+[temp]