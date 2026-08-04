class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        second = first + 1
        profit = 0

        while second < len(prices):
            #when profit is negative
            if prices[second] - prices[first] < 0:
                first += 1
            else:
                profit = max(profit, prices[second] - prices[first])
                second += 1
        return profit
