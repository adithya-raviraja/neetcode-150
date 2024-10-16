# Question Link: https://leetcode.com/problems/subarray-sum-equals-k/
from typing import *

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        count = 0
        sum_map = {0: 1}

        for i in range(0, len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in sum_map:
                count += sum_map[(curr_sum - k)]

            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1

        print(sum_map)
        return count

if __name__ == "__main__":
    input = [2,1,4,3,1]
    k = 3

    res = Solution().subarraySum(input, k)
    print('RES: ', res)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')