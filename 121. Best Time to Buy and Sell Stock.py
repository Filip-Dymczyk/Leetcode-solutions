from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy_idx = 0
        sell_idx = 1

        while sell_idx < len(prices):
            if prices[sell_idx] - prices[buy_idx] > 0:
                profit = max(prices[sell_idx] - prices[buy_idx], profit)
            else:
                buy_idx = sell_idx
            sell_idx += 1
        return profit
