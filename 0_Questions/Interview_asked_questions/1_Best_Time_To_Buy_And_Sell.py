#Statement : You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# O(n) time complexity
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Example 1 Output:", solution.maxProfit(prices1))





"""
Example Walkthrough:
For prices = [7, 1, 5, 3, 6, 4]:

Day 0 (7): min_price = 7, max_profit = 0

Day 1 (1): min_price = 1 (since 1 < 7), max_profit = 0

Day 2 (5): 5 - 1 = 4 > 0 → max_profit = 4

Day 3 (3): 3 - 1 = 2 (not > 4) → no update

Day 4 (6): 6 - 1 = 5 > 4 → max_profit = 5

Day 5 (4): 4 - 1 = 3 (not > 5) → no update

Final result: 5 (buy at 1, sell at 6).
"""