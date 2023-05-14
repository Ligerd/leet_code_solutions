from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            elif current_price - min_price > max_profit:
                max_profit = current_price - min_price
        return max_profit
