def removeElement(nums, val):
    i, k = 0, 0
    while i <= len(nums)-1:
        if nums[i] != val:
            nums[k] = nums[i]
            k = k + 1
        i = i + 1
    return k

nums = [1, 0, 0, 0, 2, 5, 6, 8, 9]
val = 0

size = removeElement(nums, val)

print(f"Size = {size}")
print("nums = ")
for n in nums:
    print(f"{n}", end=" ")