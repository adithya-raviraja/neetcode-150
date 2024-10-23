# Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import *

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[j-2] != nums[i] or j == 1:
                nums[j] = nums[i]
                j = j + 1

        return int(j)

if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    # nums = [1,1,1,2,2,3] 
    output = Solution().removeDuplicates(nums)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')