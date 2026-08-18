class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
    
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i+k]

            for x in set(subarray):
                count[x] = count.get(x, 0) + 1

        almost_missing = []

        for x in count:
            if count[x] == 1:
                almost_missing.append(x)

        if almost_missing:
            return max(almost_missing)

        return -1