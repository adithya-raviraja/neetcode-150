# Question Link: https://neetcode.io/problems/two-integer-sum-ii
from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        two_sum_array = list()
        left = 0
        right = len(numbers) - 1
        while left < right:
            if (numbers[left] + numbers[right]) > target:
                right = right - 1
            elif (numbers[left] + numbers[right]) < target:
                left = left + 1
            else:
                two_sum_array.append(left + 1)
                two_sum_array.append(right + 1)
                break
        return two_sum_array

if __name__ == "__main__":
    numbers = [1,2,3,4]
    target = 3

    output = Solution().twoSum(numbers, target)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')