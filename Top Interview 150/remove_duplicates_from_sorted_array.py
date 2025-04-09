def removeDuplicates(nums):
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k = k + 1
                nums[k] = nums[i]
        return k + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k = removeDuplicates(nums)

print("nums = ")
for n in nums[:k]:
    print(f"{n}", end=" ")