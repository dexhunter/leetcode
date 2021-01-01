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

class Solution2:
    def plusOne(self, digits):
        """recursion
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits

class Solution3(object):
    def plusOne(self, digits):
        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return self.plusOne(digits[:-1])+[0]