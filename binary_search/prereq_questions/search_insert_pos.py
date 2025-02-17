# Question Link: https://leetcode.com/problems/search-insert-position/
from typing import *

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        
        if target < nums[mid]:
            return mid
        else:
            return mid + 1


        

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5

    output = Solution().searchInsert(nums, target)
    print(output)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')