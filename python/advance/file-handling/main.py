# file_name = 'multi-lines.txt'
# # open(file_name, 'w')

# try:
#     # file = open(file_name, 'w')
#     # file = open(file_name, 'a')
#     # file = open(file_name, 'x')
#     file = open(file_name, 'r')
# except FileExistsError:
#     print(f"File {file_name} already exists.")
# except NameError:
#     print("Variable 'file_name' is not defined.")
# except Exception as err:
#     print(f"Error: {err}")
# else:
#     # file.write(input("Enter somethning... "))
#     # print(file.read()) # read whole file data
#     # print(file.read(7))
#     # print(file.readline())
#     # print(file.readline())
#     # print(file.readline())
#     # print(file.readline())
#     # print(file.readline())
#     # print(file.readline())

#     lines = file.readlines() + list((
#         '\nthis is my new line 1',
#         '\nthis is my new line 2',
#         '\nthis is my new line 3',
#         '\nthis is my new line 4',
#         '\nthis is my new line 5',
#         '\nthis is my new line 6',
#     ))

#     mlfile = open(file_name, 'w')
#     mlfile.writelines(lines)
# finally:
#     print("I will be execute anyway.")
#     file.close()
#     mlfile.close()

print(a)
