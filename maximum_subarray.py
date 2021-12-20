# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubArray1(nums):
    max_so_far = nums[0]
    max_value = nums[0]
    
    for i in range(1, len(nums)):
        max_so_far = max(max_so_far + nums[i], nums[i])
        max_value = max(max_value, max_so_far)
        
    return max_value 

# Divide and Conquer Approach
def maxSubArray2(nums):
    
    def maxsubarray(arr, left, right):
        if left > right:
            return float("-inf")
        mid = (left + right)//2
        left_sum, right_sum  = 0, 0
        cur_sum = 0
        
        for i in range(mid-1, left-1, -1):
            cur_sum += arr[i]
            left_sum = max(left_sum, cur_sum)
        
        cur_sum = 0
        for i in range(mid+1, right+1):
            cur_sum += arr[i]
            right_sum = max(right_sum, cur_sum)
        
        return max(maxsubarray(arr, left, mid-1), maxsubarray(arr, mid+1, right), left_sum + arr[mid] + right_sum)
    
    return maxsubarray(nums, 0, len(nums)-1)
    


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
            
        if max_so_far > max_value :
            endIdx = i
            max_value = max_so_far
    
    return endIdx - startIdx + 1             
        
    