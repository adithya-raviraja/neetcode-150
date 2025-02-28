# Question Link: 
from typing import *

class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def split(nums, largest_sum):
            pieces = 1
            tmp_sum = 0

            for num in nums:
                if (tmp_sum + num) > largest_sum:
                    tmp_sum = num
                    pieces += 1
                else:
                    tmp_sum = tmp_sum + num
            
            return pieces
        
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            pieces = split(nums, mid)
            if pieces > k:
                low = mid + 1
            else:
                high = mid
        
        return low

        
if __name__ == "__main__":
    nums = [7,2,5,10,8]
    k = 2
    output = Solution().splitArray(nums, k)
    print(output)
    print('TIME COMPLEXITY: O(nlogn)')
    print('SPACE COMPLEXITY: O(1)')