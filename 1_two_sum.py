def two_sum(nums, target):
    """
    uses hashmap to return position of two numbers in given list that give together sum of target
    time complexity O(n)
    :param nums: List[int]
    :param target: int
    :rtype: List[int]
    """

    hashmap = {}
    for i, num in enumerate(nums):
        rest = target - num

        if str(rest) in hashmap:
            return [hashmap[str(rest)], i]

        else:
            hashmap[str(num)] = i


my_list = [2, 7, 11, 15]
print(two_sum(my_list, 9))
