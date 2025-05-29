def removeDuplicates(nums):
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k = k + 1
        return k

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

k = removeDuplicates(nums)

print("nums = ")
for n in nums[:k]:
    print(f"{n}", end=" ")