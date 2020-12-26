class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        min_price = prices[0]
        profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > profit:
                profit = i - min_price
        
        return profit
