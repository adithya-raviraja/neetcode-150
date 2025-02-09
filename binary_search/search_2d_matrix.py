# Question Link: 
from typing import *

class Solution:
    def searchArray(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return True
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self.searchArray(matrix[mid], target)
    
        return False

if __name__ == "__main__":
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 14
    output = Solution().searchMatrix(matrix, target)
    print('Output: ', output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')