class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using greedy solution
        # no need to loop through the whole list to find the best profit
        # just adds up the profit between neibors
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]: 
                profit += prices[i + 1] - prices[i]
        return profit