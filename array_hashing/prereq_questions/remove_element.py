# Question Link: https://leetcode.com/problems/remove-element/
from typing import *

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        swap_var = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                swap_var = nums[j]
                nums[j] = nums[i]
                nums[i] = swap_var
                j = j + 1
            i = i + 1

        return int(j)


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print('INPUT: ', nums)
    count = Solution().removeElement(nums, val)
    print('OUTPUT: ', nums, ' count: ', count)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')