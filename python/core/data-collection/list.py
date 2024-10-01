"""
List - mutable, ordered, duplicate values are allowed, indexing, slicing, store any type of data

syntax: 
list_name = []
list_name = list()

"""
# list = list()
# print(type(list))
# print(len(list))

# nums = [1,2,3,4,5]
# nums = [10]
# for ele in nums:
#     print(ele)

# mix_data = [10, 20.4, "ghfasdfasA@", 34 + 765j]
# print(mix_data)

# nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,4]
# print(nums)

# Accessing a list elements
# Access full list
# print(nums)

# Access specific index (+/-)
# print(nums[0])
# print(nums[1])
# print(nums[-1])
# print(nums[-2])

# for index, element in enumerate(nums):
#     # print(nums[index])
#     print(f"Index: {index}, Element: {element}")

# Slicing (+/-)
# print(nums[4:9])
# print(nums[4:9:-1])
# print(nums[4:9][::-1])
# print(nums[-2:-7:-1])

# update list
# a = [1111]
# b = [1,2,3,4,5]
# a[0] = b[1]
# print(a[0])



chs = ['a', 'b', 'c', 'd', 'e']
# print(dir(chs))


# add elements in a list
# new_chs = ['f','g','h']
# new_chs = "f"
# chs.append(new_chs)
# chs.extend(new_chs)
# chs.insert(2, new_chs)
# print(chs)

# update elements in a list
# chs[0] = 'AAAAA'
# print(chs)

# delete elements in a list
# chs.remove('a')
# chs.remove('z') # ValueError: list.remove(x): x not in list
# del chs[0]
# chs.pop(0)
# chs.clear()
# print(chs)

# users = []
# user = []
# for u in range(1, 3):
#     name = input(f"Enter name for user {u}: ")
#     age = int(input(f"Enter age for user {u}: "))
#     user.append(name)
#     user.append(age)
#     print(user)
#     users.append(user)
#     user.clear()

# print(users)

# mix 
# print(chs.index('d'))

nums = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,4]
# nums.reverse()

# print(nums.count(4))

# nums.sort(reverse=True)
# print(nums)

# print(nums.index(4))
# print(nums.index(4, 4))
# print(nums.index(4, 14))

# num1 = 10
# num2 = 20
# num3 = 10
# # print(id(num1), id(num2))
# print(id(num1), id(num3))

# num1 = [1,2,3,4,5]
# num2 = num1.copy()
# print(num1)
# print(num2)
# print(id(num1))
# print(id(num2))


nums = [10, 20, [30, 40, [50, 60, 60, [70, 80,[90]]]]]
# print(nums[-1])  
print(nums[-1][-1])  
print(nums[-1][-1][-1])  
print(nums[-1][-1][-1][-1])  
print(nums[-1][-1][-1][-1][-1])  
