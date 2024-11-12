# Question Link: https://leetcode.com/problems/trapping-rain-water/description/
from typing import *

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        counter = 0

        while i < (len(height) - 1) and j < (len(height) - 1):
            if i == 0 and height[i] == 0:
                i = i + 1
                j = j + 1
                continue

            if height[i] == height[j]:
                i = i + 1
                j = j + 1
            else:
                last_entry = False if j + 1 < (len(height) - 1) else True

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')