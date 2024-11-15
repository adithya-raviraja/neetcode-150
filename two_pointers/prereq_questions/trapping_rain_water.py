# Question Link: https://leetcode.com/problems/trapping-rain-water/description/
from typing import *

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        res = 0
        while left < right:
            if left_max < right_max:
                left = left + 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right = right - 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    output = Solution().trap(height)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')