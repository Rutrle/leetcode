def brute_force(nums, target):
    for i, num_a in enumerate(nums):
        for j, num_b in enumerate(nums[i+1:]):
            if num_b+num_a == target:
                return[i, i+j+1]

def hash_map_solution(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target-num in hash_map:
            return [i, hash_map[target-num]]
        else:
            hash_map[num] = i


nums = [2,7,11,15]
target = 9

print(brute_force(nums, target))
print(hash_map_solution(nums, target))