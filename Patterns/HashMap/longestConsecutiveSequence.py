class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        length = 1
        for i, v in enumerate(nums_set):
            if v - 1 in nums_set:
                length += 1
        return length