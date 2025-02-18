# Question Link: https://neetcode.io/problems/eating-bananas
from typing import *
import math

class Solution:
    def totalHoursTaken(self, piles, bph):
        total = 0
        for pile in piles:
            total += math.ceil(float(pile) / bph)
        return total
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_speed = high

        while low <= high:
            mid = (low + high) // 2
            total_hours = self.totalHoursTaken(piles, mid)
            if total_hours <= h:
                min_speed = mid
                high = mid - 1
            else:
                low = mid + 1

        return min_speed
        
if __name__ == "__main__":
    piles = [25,10,23,4]
    h = 4
    output = Solution().minEatingSpeed(piles, h)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')