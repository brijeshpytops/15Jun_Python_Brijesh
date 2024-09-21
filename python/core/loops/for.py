"""
For loop in python?

syntax:

for variable in sequence:
    # code block to be executed for each item in the sequence
"""

# for ch in "python":
#     print(ch)

# code = "python"
# ch_iter = iter(code)
# print(next(ch_iter))
# print(next(ch_iter))
# print(next(ch_iter))
# print(next(ch_iter))
# print(next(ch_iter))
# print(next(ch_iter))
# print(next(ch_iter))

# * * * * *
#   *       *
#     *   -   *
#       *       *
#         * * * * *

# num = 5
# flag = int((num/2) + .5 )
# for row in range(1, num+1):
#     for s_col in range(1, row):
#         print(" ", end=" ")
#     for p_col in range(1, num+1):
#         if row == 1 or row == num or p_col == 1 or p_col == num:
#             print("*", end=" ")
#         else:
#             if p_col == flag and row == flag:
#                 print("-", end=" ")
#             else:
#                 print(" ", end=" ")
#     print()

#         * * * * *
#       *       *
#     *   -   *
#   *       *
# * * * * *
# num = 5
# flag = int((num/2) + .5 )
# for row in range(1, num+1):
#     for s_col in range(1, num-row+1):
#         print(" ", end=" ")
#     for p_col in range(1, num+1):
#         if row == 1 or row == num or p_col == 1 or p_col == num:
#             print("*", end=" ")
#         else:
#             if p_col == flag and row == flag:
#                 print("-", end=" ")
#             else:
#                 print(" ", end=" ")
#     print()

# num = 5
# for dash in range(1, num):
#     print("-", end="")
# for equal in range(1, num+1):
#     print("=", end="")

# num = 5
# flag = int((num/2) + .5 )
# for counter in range(1, num+1):
#     if counter % 2 != 0:
#         for row in range(1, num+1):
#             for s_col in range(1, row):
#                 print(" ", end=" ")
#             for p_col in range(1, num+1):
#                 if row == 1 or row == num or p_col == 1 or p_col == num:
#                     print("*", end=" ")
#                 else:
#                     if p_col == flag and row == flag:
#                         print(f"{counter}", end=" ")
#                     else:
#                         print(" ", end=" ")
#             print()
#         if counter < num:
#             for dash in range(1, num):
#                 print(" ", end=" ")
#             for equal in range(1, num+1):
#                 print("=", end=" ")
#             print()
#     else:
#         for row in range(1, num+1):
#             for s_col in range(1, num-row+1):
#                 print(" ", end=" ")
#             for p_col in range(1, num+1):
#                 if row == 1 or row == num or p_col == 1 or p_col == num:
#                     print("*", end=" ")
#                 else:
#                     if p_col == flag and row == flag:
#                         print(f"{counter}", end=" ")
#                     else:
#                         print(" ", end=" ")
#             print()

#         for equal in range(1, num+1):
#             print("=", end=" ")
#         print()

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print(ord(chr(col + 96)), end=" ")
#     print()


# 0 1 1 1 1
# 1 0 1 1 1
# 1 1 0 1 1
# 1 1 1 0 1
# 1 1 1 1 0

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row == col:
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# 1 1 1 1 0
# 1 1 1 0 1
# 1 1 0 1 1
# 1 0 1 1 1
# 0 1 1 1 1

# num = 5
# for row in range(num, 0, -1):
#     for col in range(1, num+1):
#         if row == col:
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()


# 1 1 0 1 1
# 1 1 0 1 1
# 0 0 0 0 0
# 1 1 0 1 1
# 1 1 0 1 1


# num = 5
# flag = num//2 + 1
# if num %2 != 0:
#     for row in range(num, 0, -1):
#         for col in range(1, num+1):
#             if row == flag or col == flag:
#                 print("0", end=" ")
#             else:
#                 print("1", end=" ")
#         print()
# else:
#     print("number should be odd.")

# 0 1 1 1 0
# 1 0 1 0 1
# 1 1 0 1 1
# 1 0 1 0 1
# 0 1 1 1 0

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row == col or (num-(row-1)== col):
#             print("0", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# num = 9
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row == 1 or row == num or col == 1 or col == num:
#             print("*", end=' ')
#         else:
#             if col % 2 == 0 or row % 2 == 0 and col <= row:
#                 if row 
#                 print(" ", end=' ')
#             else:
#                 print("*", end=' ')
            
#     print()

# * * * * * * * * *
# *   *   *   *   *
# * * *   *   *   *
# *       *   *   *
# * * * * *   *   *
# *           *   *
# * * * * * * *   *
# *               *
# * * * * * * * * *

num = 9
for row in range(1, num+1):
    for col in range(1, num+1):
        if row == 1 or row == num or col == 1 or col == num:
            print("*", end=' ')
        else:
            if (row % 2 == 0 and col <= row) or (col % 2 == 0):
                if row <= col: 
                    print(" ", end=' ')
                else:
                    if row %2 != 0:
                        print("*", end=' ')
                    else:
                        print(" ", end=" ")
            else:
                print("*", end=' ')
    print()

