class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        r = {}

        for i, seat in reservedSeats:
            if i not in r:
                r[i] = set()
            r[i].add(seat)
        ans = 2 * n

        for i in r:
            reserved = r[i]

            left = {2,3,4,5}
            middle = {4,5,6,7}
            right = {6,7,8,9}

            left_free = not(left & reserved)
            right_free = not(right & reserved)
            middle_free = not(middle & reserved)

            if left_free and right_free:
                continue
            elif left_free or right_free:
                ans -= 1
            elif middle_free:
                ans -= 1
            else:
                ans -= 2
        return ans

