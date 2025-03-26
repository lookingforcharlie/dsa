class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You don't recompute the profit for days that have already passed
        # Dynamically trace the min price in the array 
        # min price actually doesn't effect the max profit 
        # Take prices_2 = [4, 17, 1, 5, 3, 6, 4] as example, max profit actually happens between 4 and 17
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit