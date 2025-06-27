def merge_array(nums1, nums2, m, n):
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1
    while p1 >=0 and p2 >=0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 = p2 - 1
        else:
            nums1[p] = nums1[p1]
            p1 = p1 - 1
        p = p - 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 = p2 - 1
        p = p - 1

nums1 = [1,2,3,4,0,0]
nums2 = [2,5,6]
m = 3
n = 3

merge_array(nums1, nums2, m, n)

for n in nums1:
    print(f"{n}", end=" ")