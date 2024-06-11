# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

nums = [23,2,4,6,7]
k = 6
size = len(nums)
if len(nums) <=1:
    print(False)

sum_index ={0:-1}   
cur_sum =0
for i in range(size) :
    cur_sum += nums[i]
    cur_sum %=k
    if cur_sum  not in sum_index:
                sum_index[cur_sum] = i
    elif i - sum_index[cur_sum] >= 2:
                print (True)
print (False)
    
