# Question Link: https://leetcode.com/problems/3sum/description/
from typing import *

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        three_sum_list = list()
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                three_sum = value + nums[left] + nums[right]
                if three_sum < 0:
                    left = left + 1
                elif three_sum > 0:
                    right = right - 1
                else:
                    entry_to_add = [value, nums[left], nums[right]]
                    entry_to_add.sort()
                    if entry_to_add not in three_sum_list:
                        three_sum_list.append(entry_to_add)

                    left = left + 1

        return three_sum_list

if __name__ == "__main__":
    nums = [0,0,0]
    output = Solution().threeSum(nums)
    print(output)
    print('TIME COMPLEXITY: ')
    print('SPACE COMPLEXITY: ')