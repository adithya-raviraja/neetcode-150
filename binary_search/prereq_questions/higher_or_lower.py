# Question Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/
from typing import *
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pick = 6
    if num == pick:
        return 0 
    if num < pick:
        return -1
    if num > pick:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n

        while low <= high:
            mid = (low + high) // 2
            output = guess(mid)

            if output == 0:
                return mid
            elif output == 1:
                low = mid + 1
            else:
                high = mid - 1

        return -1
            

if __name__ == "__main__":
    n = 10
    output = Solution().guessNumber(n)
    print(output)

    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')