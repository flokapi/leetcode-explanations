"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        max_sell = 0
        best_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            val = prices[i]
            best_profit = max(best_profit, max_sell - val)
            max_sell = max(max_sell, val)

        return best_profit


class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy = float("inf")
        best_profit = 0

        for val in prices:
            best_profit = max(best_profit, val - min_buy)
            min_buy = min(min_buy, val)

        return best_profit


class Solution:
    """
    Keep the value of the min_buy and best_profit
    Initial min_buy is infinite, to ensure the first value will be next
    Iteratively, first update the best_profit givent the current sell value
    Then, update the min_buy value if necessary
    """

    def maxProfit(self, prices: list[int]) -> int:
        min_buy = float("inf")
        best_profit = 0

        for val in prices:
            if val - min_buy > best_profit:
                best_profit = val - min_buy
            if val < min_buy:
                min_buy = val

        return best_profit


class Solution2P:
    """
    Two pointer solution
    If configuration enables profit, update best profit if better
    Otherwise, we found a lower point => restart from that point
    Move the right pointer to see if a better profit is possible
    """

    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        best_profit = 0

        while right != len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > best_profit:
                    best_profit = profit
            else:
                left = right
            right += 1

        return best_profit


prices = [7, 1, 5, 3, 6, 4]  # -> 5
# prices = [7, 6, 4, 3, 1]  # -> 0
solution = Solution2P()
res = solution.maxProfit(prices)
print(res)
