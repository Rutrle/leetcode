def contains_duplicate(array):
    hashset = []
    for item in array:
        if item in hashset:
            return True
        else:
            hashset.append(item)
    return False


my_array_1 = [1, 2, 4, 55, 8, 4, 3, 5, 4]
my_array_2 = [1, 2, 4, 55, 8, 9, 3, 5, 11]

print(contains_duplicate(my_array_1))
print(contains_duplicate(my_array_2))
