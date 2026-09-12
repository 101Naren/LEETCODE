class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and i != k:
                        if digits[i] != 0:
                            if digits[k] % 2 == 0:
                                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                                result.add(num)
        return sorted(result)