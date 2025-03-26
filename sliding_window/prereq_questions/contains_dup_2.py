# Question Link: https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import *

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = dict()

        for index, val in enumerate(nums):
            if (val in window) and (abs(index - window[val]) <= k):
                return True
            
            window[val] = index

        return False

if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    output = Solution().containsNearbyDuplicate(nums, k)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(k)')