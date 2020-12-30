class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += (prices[i] - prices[i-1])
        return profit


# greedy # same as mine
class Solution2:
    def maxProfit(self, prices):
        if not prices or len(prices) is 1:
            return 0
        
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

# dp
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0