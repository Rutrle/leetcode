from sys import prefix


def brute_force(nums):
    products=[]
    for i, num in enumerate(nums):
        product = 1
        for  num_p in nums[:i]:
            product = product*num_p

        for  num_a in nums[i+1:]:
            product = product*num_a

        products.append(product)

    return products

def two_passes(nums):
    results = [1]
    for num in nums[:-1]:
        results.append(results[-1]*num)

    post = 1
    for i in range(len(nums)-1,-1,-1):
        results[i] = results[i]*post
        post =post * nums[i]
        
    print(results)

def nice_solution(nums):
    res = [1]*len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *=nums[i]

    return res


nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
nums3 = [-1,1,2,-3,3]
print('_'*50)
print(brute_force(nums))
print(brute_force(nums2))
print(brute_force(nums3))
print('_'*50)
print(two_passes(nums))
print(two_passes(nums2))
print('_'*50)
print(nice_solution(nums))
print(nice_solution(nums2))