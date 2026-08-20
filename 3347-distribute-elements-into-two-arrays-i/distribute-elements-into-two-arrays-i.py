class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one = [nums[0]]
        two = [nums[1]]

        for i in range (2, len(nums)):
            if one[-1] > two[-1]:
                one.append(nums[i])
            else:
                two.append(nums[i])
        
        ans = one + two
        
        return ans