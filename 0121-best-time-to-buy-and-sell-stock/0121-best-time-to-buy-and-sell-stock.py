class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# One linear lop: O(n)
        buy_price = prices[0]
        current_profit = 0
        max_profit = 0
        for i in range(len(prices)): 
            if prices[i] <= buy_price: 
                buy_price = prices[i] 
            elif prices[i] > buy_price: 
                current_profit = prices[i] - buy_price
            if current_profit > max_profit: 
                max_profit = current_profit
        if max_profit > 0: 
            return max_profit
        else: 
            return 0 
        
        
        
# Original approach: Nested a for loop inside a for loop. 
# Big O Notatio: O(n^2) or O(N)
        # max_profit = 0
        # for i in range(len(prices)): 
        #     for j in range(i + 1, len(prices)):
        #         if  prices[j] - prices[i] > max_profit: 
        #             max_profit = prices[j] - prices[i]
        # if max_profit > 0: 
        #     return max_profit
        # else: 
        #     return 0 