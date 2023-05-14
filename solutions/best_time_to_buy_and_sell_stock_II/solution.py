from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for price_index in range(1, len(prices)):
            if prices[price_index] > prices[price_index - 1]:
                max_profit += prices[price_index] - prices[price_index - 1]
        return max_profit
