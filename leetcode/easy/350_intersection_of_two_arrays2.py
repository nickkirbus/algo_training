def intersect(nums1, nums2):
    division_qty_nums = abs(len(nums1) - len(nums2))
    j=0
    small_integer = -1
    if len(nums1) > len(nums2):

        while division_qty_nums != j:
            nums2.append(small_integer)
            j += 1
    else:
        while division_qty_nums != j:
            nums1.append(small_integer)
            j += 1
    nums2.sort()
    nums1.sort()
    print(nums1)
    print(nums2)
    for i in range(len(nums1)):
        if nums1[i]!= -1:
            # print(nums1)
            # print(nums2)
            if nums1[i] != nums2[i]:
                nums1[i] = -1
            else:
                nums2[i] = -1


    res = []
    for num in nums1:
        if num != -1:
            res.append(num)
    return res

print(intersect([4,9,5], [9,4,9,8,4]))