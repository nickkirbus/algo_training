def minDifference(nums) -> int:
    if len(nums) < 4:
        return 0

    left = 0
    right = len(nums) -1

    nums.sort()
    min_diff = nums[-1] - nums[0]
    i=0
    while i!=3:
        if nums[right] - nums[left] >= min_diff:
            left += 1
        else:
            right -= 1
        i += 1
    return nums[right] - nums[left] 
    


print(minDifference([6,6,0,1,1,4,6]))