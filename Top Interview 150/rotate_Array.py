def rotate(nums, k):
    n = len(nums)
    if k > n:
        k %= n

    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1

    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
modnums = rotate(nums, k)

for n in modnums:
    print(f"{n}", end=" ")