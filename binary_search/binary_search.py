# Question Link: https://neetcode.io/problems/binary-search
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        return -1

if __name__ == "__main__":
    nums = [-1,0,2,4,6,8]
    target = 4

    index = Solution().search(nums, target)
    print('RESULT: ', index)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')