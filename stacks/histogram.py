# Question Link: https://neetcode.io/problems/largest-rectangle-in-histogram
from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area_stack = list()
        max_area = -1

        for index, height in enumerate(heights):
            start = index
            while area_stack and area_stack[-1][1] > height:
                prev_entry = area_stack.pop()
                stack_height = prev_entry[1]
                stack_index = prev_entry[0]
                max_area = max(max_area, stack_height * (index - stack_index))
                start = stack_index

            area_stack.append([start, height])
        
        for i, h in area_stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area



if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    area = Solution().largestRectangleArea(heights)
    print(area)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')