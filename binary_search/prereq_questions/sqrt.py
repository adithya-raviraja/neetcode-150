# Question Link: https://leetcode.com/problems/sqrtx/
from typing import *

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) > x:
                high = mid - 1
            elif (mid * mid) < x:
                low = mid + 1
            else:
                return mid
            
        return low - 1

if __name__ == "__main__":
    sqrt = Solution().mySqrt(4)
    print(sqrt)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')