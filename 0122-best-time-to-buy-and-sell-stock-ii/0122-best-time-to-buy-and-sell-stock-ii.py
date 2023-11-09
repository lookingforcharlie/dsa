class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(len(prices) -1): 
            if prices[i + 1] > prices[i]: 
                profit += prices[i + 1] - prices[i]
        return profit
        
# make buy and sell as many as possible 
# If the next item is greater than the previous item, make buy and sell
# Draw a picture of stock market price/day helps understand the problem
        
    