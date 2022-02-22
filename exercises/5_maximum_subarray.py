#brute force 
from math import inf


def brute_force(nums:list)->int:
    maximum=float(-inf)
    for i in range(len(nums)):
        for j in range(len(nums[i:])):
            subarray_sum = sum(nums[i:j+i+1])
            #O(n3) because of the sum
            if subarray_sum>maximum:
                maximum = subarray_sum

    return maximum

def lesser_brute_force(nums:list)->int:
    maximum=float(-inf)
    for i in range(len(nums)):
        subarray_sum = nums[i]
        if subarray_sum>maximum:
            maximum = subarray_sum
        for j in range(len(nums[i+1:])):
            subarray_sum +=nums[j+i+1]
            if subarray_sum>maximum:
                maximum = subarray_sum
            
            #O(n2)
    return maximum

def optimal_maximum_subarray(nums):
    prefix = 0
    subarray_max = -float('inf')
    for num in nums:
        if prefix >0:
            subarray_sum=prefix + num
        else:
            subarray_sum = num
        prefix = subarray_sum
        if subarray_sum> subarray_max:
            subarray_max= subarray_sum

    return subarray_max

nums=[1,2,3]
nums2=[-2,1,-3,4,-1,2,1,-5,4]

print(brute_force(nums))
print(brute_force(nums2))

print(lesser_brute_force(nums))
print(lesser_brute_force(nums2))

print(optimal_maximum_subarray(nums))
print(optimal_maximum_subarray(nums2))