# Question Link: https://neetcode.io/problems/buy-and-sell-crypto
from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxP = 0
        
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
        
        return maxP
                


if __name__ == "__main__":
    prices = [10,8,7,5,2]
    output = Solution().maxProfit(prices)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')