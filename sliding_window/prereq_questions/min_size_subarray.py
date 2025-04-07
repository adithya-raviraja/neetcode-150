# Question Link: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1587605441/
from typing import *

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = float('inf')
        L = 0
        sum_arr = 0

        for R in range(len(nums)):
            sum_arr += nums[R]
            while sum_arr >= target:
                length = min(length, R - L + 1)
                sum_arr -= nums[L]
                L += 1
        
        return 0 if length == float('inf') else length

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]

    output = Solution().minSubArrayLen(target, nums)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')