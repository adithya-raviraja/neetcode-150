# Question Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import *
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return True

            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                l += 1
        return False
        

if __name__ == "__main__":
    nums = [1,0,1,1,1]
    target = 0
    output = Solution().search(nums, target)
    print(output)
    print('TIME COMPLEXITY: O(logn)')
    print('SPACE COMPLEXITY: O(1)')