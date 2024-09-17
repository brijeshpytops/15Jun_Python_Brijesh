
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 5
# row = 1
# col = 1
# while(row <= num):
#     while(col <= num):
#         print("*", end=" ")
#         col+=1
#     row+=1
#     col = 1
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# num = 5
# row = 1
# col = 1
# while(row <= num):
#     while(col <= row):
#         print("*", end=" ")
#         col+=1
#     row+=1
#     col = 1
#     print()


# * * * * *
# * * * *
# * * *
# * *
# *


# num = 5
# row = 1
# col = 5
# while(row <= num):
#     while(col >= row):
#         print("*", end=" ")
#         col-=1
#     row+=1
#     col = 5
#     print()



# * * * * *
# *       *
# *   1   *
# *       *
# * * * * *
# =========
# * * * * *
# *       *
# *   2   *
# *       *
# * * * * *
# =========
# * * * * *
# *       *
# *   3   *
# *       *
# * * * * *
# =========
# * * * * *
# *       *
# *   4   *
# *       *
# * * * * *
# =========
# * * * * *
# *       *
# *   5   *
# *       *
# * * * * *



# num = 5

# flag = int((num/2) + .5 )

# if num % 2 != 0:
#     for counter in range(1, num+1):
#         for row in range(1, num+1):
#             for col in range(1, num+1):
#                 if row == 1 or row == num or col == 1 or col == num:
#                     print("*", end=" ")
#                 else:
#                     if row == flag and col == flag:
#                         print(f"{counter}", end=" ")
#                     else:
#                         print(" ", end=" ")
#             print()
#         if counter < num:
#             for equal in range(1, num*2):
#                 print("=", end="")
#             print()
# else:
#     print("Number should be odd.")
