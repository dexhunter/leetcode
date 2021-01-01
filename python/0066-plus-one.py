class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        num = int(num) + 1
        result = []
        for i in str(num):
            result.append(int(i))
        if len(digits) != len(result):
            for i in range(len(digits)-len(result)):
                result.insert(0,0)
        return result
        