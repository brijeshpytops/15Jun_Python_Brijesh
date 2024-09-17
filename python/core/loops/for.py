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

num = 5
flag = int((num/2) + .5 )
for counter in range(1, num+1):
    if counter % 2 != 0:
        for row in range(1, num+1):
            for s_col in range(1, row):
                print(" ", end=" ")
            for p_col in range(1, num+1):
                if row == 1 or row == num or p_col == 1 or p_col == num:
                    print("*", end=" ")
                else:
                    if p_col == flag and row == flag:
                        print(f"{counter}", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        if counter < num:
            for dash in range(1, num):
                print(" ", end=" ")
            for equal in range(1, num+1):
                print("=", end=" ")
            print()
    else:
        for row in range(1, num+1):
            for s_col in range(1, num-row+1):
                print(" ", end=" ")
            for p_col in range(1, num+1):
                if row == 1 or row == num or p_col == 1 or p_col == num:
                    print("*", end=" ")
                else:
                    if p_col == flag and row == flag:
                        print(f"{counter}", end=" ")
                    else:
                        print(" ", end=" ")
            print()

        for equal in range(1, num+1):
            print("=", end=" ")
        print()