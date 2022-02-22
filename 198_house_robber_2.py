def rob(nums: list) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n+rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


print(rob([2, 7, 9, 3, 1]))
# https: // www.youtube.com/watch?v = 73r3KWiEvyk
print(rob([1, 2, 4, 55, 8, 9, 3, 5, 11]))
