# Question Link: https://leetcode.com/problems/find-pivot-index/
from typing import *

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = list()
        postfix = list()
        index_array = list()
        total_sum_prefix = 0
        total_sum_postfix = 0
        for i in range(0, len(nums)):
            if i == 0:
                total_sum_prefix += 0
            else:
                total_sum_prefix += nums[i-1]

            # if i == len(nums) - 1:
            #     total_sum_postfix += 0
            # else:
            #     total_sum_postfix += nums[(len(nums) - 1) - i]
            prefix.append(total_sum_prefix)
            # postfix.append(total_sum_postfix)

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                total_sum_postfix += 0
            else:
                total_sum_postfix += nums[i + 1]

            postfix.append(total_sum_postfix)

        # print('INPUT: ', input)
        # print('PREFIX: ', prefix)
        # print('POSTFIX: ', postfix)

        for index, value in enumerate(nums):
            if index == 0:
                left_sum = 0
            else:
                left_sum = prefix[index]

            if index == len(nums) - 1:
                right_sum = 0
            else:
                right_sum = postfix[len(nums) - 1 - index]

            # print(f'INDEX: {index}, LEFT: {left_sum}, RIGHT: {right_sum}, index_val: {nums[index]}')
            left_sum = left_sum - nums[index]
            right_sum = right_sum - nums[index]
            if left_sum == right_sum:
                # print('EQUAL')
                index_array.append(index)
            else:
                # print('NOT EQUAL')
                pass            
        
        if len(index_array) == 0:
            return -1
        else:
            return index_array[0]


if __name__ == "__main__":
    input = [1,7,3,6,5,6]
    # input = [2,1,-1]
    # input = [1,2,3]
    pivot_index = Solution().pivotIndex(input)
    print(pivot_index)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')