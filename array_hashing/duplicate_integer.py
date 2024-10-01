from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if hash_map.get(str(num), None) == None:
                hash_map[str(num)] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1,2,3,3]
    output = Solution().hasDuplicate(nums)
    print('TEST CASE1: ', output)

    nums = [1,2,3,4]
    output = Solution().hasDuplicate(nums)
    print('TEST CASE2: ', output)
    print('TIME COMPLEXITY: O(n)')
    print('SPACE COMPLEXITY: O(n)')