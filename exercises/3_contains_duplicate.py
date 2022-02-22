def total_brute_force(nums):
    #O(n2) time
    #O(1) space
    while nums:
        current = nums.pop()
        for num in nums:
            if num == current:
                return True
    return False

def using_set(nums):
    #best in time, slightly worse in space
    control=set()
    for num in nums:
        if num in control:
            return True
        control.add(num)

    return False

#another solution is sort and then check with O(n) - probably O(nlogn)