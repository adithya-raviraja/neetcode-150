# Question Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        min_val = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                min_val = min(min_val, nums[low])
                break

            mid = (low + high) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return min_val

if __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    min_val = Solution().findMin(nums)
    print(min_val)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')