class Solution(object):
    def longestConsecutive(self, nums):
        """
        Find the length of the longest consecutive sequence in an unsorted array.

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        max_length = 1

        for v in nums_set:
            # Start counting only if v is the beginning of a sequence
            if v - 1 not in nums_set:
                length = 1
                current = v

                while current + 1 in nums_set:
                    length += 1
                    current += 1

                max_length = max(max_length, length)

        return max_length


if __name__ == "__main__":
    solution = Solution()

    nums1 = [100, 4, 200, 1, 3, 2]
    print("Input:", nums1)
    print("Longest consecutive sequence length:", solution.longestConsecutive(nums1))

    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print("Input:", nums2)
    print("Longest consecutive sequence length:", solution.longestConsecutive(nums2))

    nums3 = []
    print("Input:", nums3)
    print("Longest consecutive sequence length:", solution.longestConsecutive(nums3))