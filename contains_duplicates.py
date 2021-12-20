# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

def containDuplicates1(nums):
    if len(nums) <= 1:
        return False
    HashMap = {}
    for num in nums:
        if num in HashMap:
            return True
        HashMap[num] = True
    return False

def containDuplicates2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    
    return False

def containDuplicates3(nums):
    return len(set(nums)) != len(nums)