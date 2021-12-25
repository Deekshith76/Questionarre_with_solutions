# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

 

# Constraints:
#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000
from collections import Counter

def intersect1(nums1, nums2):
    hashMap = dict()
    for num in nums1:
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1
    lst = []
    for num in nums2:
        if num in hashMap and hashMap[num] > 0:
            lst.append(num)
            hashMap -= 1
    
    return lst

def intersect2(nums1, nums2):
    c = Counter(nums1)
    output = []
    for num in nums2:
        if c[num] > 0:
            output.append(num)
            c[num] -= 1
    
    return output
    # Time Complexity: O(n+m)
    # Space Complexity: O(n)
    
# What if arrays are sorted 
def intersect3(nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    i, j = 0, 0
    output = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            output.append(nums1[i])
            i += 1
            j += 1
            
    return output