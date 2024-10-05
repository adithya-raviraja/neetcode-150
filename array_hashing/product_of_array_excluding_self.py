from typing import *
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        index = 0
        while index < len(nums):
            res.append(1)
            index += 1
        
        for index in range(1, len(nums)):
            res[index] = res[index - 1] * nums[index - 1]

        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            res[index] *= postfix
            postfix *= nums[index]

        return res
if __name__ == "__main__":
    nums =  [-1,0,1,2,3]
    output = Solution().productExceptSelf(nums)
    print(output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(1)')