import copy


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j = j + 1
            else:
                continue

        return int(j)
        
if __name__ == "__main__":
    input = [0,0,1,1,1,2,2,3,3,4]
    print('INPUT BEFORE DUPLICATE: ', input, ' LEN: ', len(input))
    new_len = Solution().removeDuplicates(input)
    print('INPUT AFTER DUPLICATE: ', input, ' LEN: ', new_len)