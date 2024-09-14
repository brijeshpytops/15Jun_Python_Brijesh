# left to right
# range(start, stop+1, step+1)

# print(range(10)) # range(0, 10)
# print(range(1, 10)) # range(1, 10)
# print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1, 10+1))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1, 10+1, 1))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1, 10+1, 2))) # [1, 3, 5, 7, 9]
# print(list(range(1, 10+1, 3))) # [1, 4, 7, 10]
# print(list(range(1, 10+1, 4))) # [1, 5, 9]

# right to left
# print(list(range(1, 11, -1))) # []
# print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]

# print(list(range(-5, 6, 1))) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# print(list(range(5, -6, -1))) # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

print(list(range(5, -6, -1))[4:7]) # [1, 0, -1]
print(list(range(-5, 6, 1))[::-1]) # [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]



