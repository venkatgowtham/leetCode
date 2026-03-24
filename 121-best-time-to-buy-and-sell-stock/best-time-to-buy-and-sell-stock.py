class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = prices[0]
        value = 0

        for i in prices:

            if i > buy:
                value = max(value, i - buy)
            else:
                buy = i

        return value


        