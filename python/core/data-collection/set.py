# tokens = tuple(list(range(1, 11))) + (1,2,3,4)
# print(tokens[0])
# tokens.append(1)
# print(set(tokens))

"""
Set: mutable/immutable, unordered, duplicate values are not allowed, unindexed, slicing is not allowed, can store any type of data

syntax:

set_name = set()

set_name = {1,2,3,4,5}
"""

nums = {1,2,3}
# print(type(nums))
# nums.add(4)
# print(nums)
# print(nums[0])

# nums[0] = 111
# print(nums)

# num = frozenset(nums)
# num.add(5)
# print(nums)

# nums = set(range(1, 11))
# print(nums)

set_a = {1, 2, 3}
set_b = {3, 2, 1}

# print(set_a == set_b)  # True


# Define a set with elements in a specific order
my_set = {3, 1, 4, 2}

# Print the set
print("Original set:", my_set)

# Show that the order of the elements doesn't matter by defining the same set in a different order
another_set = {1, 2, 3, 4}

# Print the other set
print("Another set with same elements in different order:", another_set)

# Check if both sets are equal (they should be because sets are unordered)
print("Are both sets equal? ", my_set == another_set)
