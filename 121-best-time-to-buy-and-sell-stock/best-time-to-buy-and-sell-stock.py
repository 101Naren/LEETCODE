class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        smallest = prices[0]
        max_profit = 0

        for price in prices:

            if price < smallest:
                smallest = price

            profit = price - smallest

            if profit > max_profit:
                max_profit = profit

        return max_profit