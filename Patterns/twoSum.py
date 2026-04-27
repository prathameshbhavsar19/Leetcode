class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, v in enumerate(nums):
            x = target - v

            if x in seen:
                return [seen[x], i]

            seen[v] = i


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # [0, 1]