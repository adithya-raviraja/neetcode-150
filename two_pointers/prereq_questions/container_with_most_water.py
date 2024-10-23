# Question Link: https://leetcode.com/problems/container-with-most-water/
from typing import *

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        curr_area = 0

        while start < end:
            max_height = height[start] if height[start] <= height[end] else height[end]
            if start == 0 and end == len(height) - 1:
                curr_area = (end - start) * max_height
                if height[start] <= height[end]:
                    start = start + 1
                else:
                    end = end - 1
                continue
            
            temp = (end - (start)) * max_height
            if height[start] <= height[end]:
                start = start + 1
            else:
                end = end - 1

            if temp < curr_area:
                continue
            else:
                curr_area = temp

        return curr_area
if __name__ == "__main__":
    # input = [1,8,6,2,5,4,8,3,7]
    # input = [1,1]
    input = [8,7,2,1]
    output = Solution().maxArea(input)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')