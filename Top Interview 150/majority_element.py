def majorityElement(nums):
    n = len(nums)
    count = 0

    for i in range (0, n):
        if count == 0:
            init = nums[i]
        if init == nums[i]:
            count += 1
        else:
            count -= 1

    return init

nums = [2,2,1,1,1,2,2]
major = majorityElement(nums)

print(major)