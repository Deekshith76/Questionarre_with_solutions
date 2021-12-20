def len_of_maxSubArray(nums):
    startIdx = 0
    endIdx = 0
    max_so_far = nums[0]
    max_value = nums[0]
    
    for i in range(1, len(nums)):
        if max_so_far + nums[i] > nums[i]:
            max_so_far = max_so_far + nums[i]
        else:
            startIdx = i
            max_so_far = nums[i]
            
        if max_so_far > max_value:
            endIdx = i
            max_value = max_so_far
    
    return endIdx - startIdx + 1