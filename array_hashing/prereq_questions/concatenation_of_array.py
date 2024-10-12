# Question Link: https://leetcode.com/problems/concatenation-of-array/
from typing import *

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        concat_array = list()
        for i in range(0, len(nums)):
            concat_array.append(nums[i])
        
        for i in range(0, len(nums)):
            concat_array.append(nums[i])
        
        return concat_array

if __name__ == "__main__":
    input = [1,2,1]

    output = Solution().getConcatenation(input)
    print(output)

    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')