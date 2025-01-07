# Question Link: https://neetcode.io/problems/daily-temperatures
from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_res = [0] * len(temperatures)
        stack = [] # Temp, Index

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                temp_res[stack_index] = (index - stack_index)
            stack.append([temp, index])

        return temp_res

if __name__ == "__main__":
    temperatures = [30,38,30,36,35,40,28]
    output = Solution().dailyTemperatures(temperatures)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')