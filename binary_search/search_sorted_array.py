# Question Link: https://neetcode.io/problems/find-target-in-rotated-sorted-array
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    target = 1
    output = Solution().search(nums, target)
    print(output)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')