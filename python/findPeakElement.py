def findPeak(nums):
    len_array = len(nums)
    
    # Edge cases
    if len_array == 1:
        return 0
    if len_array == 2:
        if nums[0] > nums[1]:
            return 0
        else:
            return 1
    # 1231, 121
    # Main logic
    if nums[0]>nums[1]:
        return 0
    elif nums[len_array-1] > nums[len_array-2]:
        return len_array-1
    else:            
        for iter_ind in range(1, len_array-1):
            if (nums[iter_ind-1] < nums[iter_ind]) and (nums[iter_ind] > nums[iter_ind+1]):
                return iter_ind

arr = [1, 3, 4, 7, 8]
print(findPeak(arr))  
