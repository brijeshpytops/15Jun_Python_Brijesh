"""
What is string in python?

A string is a sequence of characters.

syntax:

string = "Hello World"
string = 'Hello World'
string = '''Hello World'''

Example:

name = "John"

print("Hello", name)

"""

# name = "tops"
# print("Hello", name)

name = "python"

# print(type(name))
# print(len(name))


# access string
# -------------

name = "python"

# full string
# print(name)

# ch  (+)   (-)
# p    0    -6
# y    1    -5
# t    2    -4
# h    3    -3
# o    4    -2
# n    5    -1

# using indexing(+/-)
# print(name[2])
# print(name[-2])

# using slicing(+/-)

# print(name[start : end-1 : step-1])
# print(name[2:5])
# print(name[-2:-5:-1][::-1])
# print(name[-4:])

# concat
# fname = "brijesh"
# lname = "gondaliya"
# fullname = fname+ " " +lname
# print(fullname) 

# Replica
star = "*"
# print(star*1)
# print(star*2)
# print(star*3)
# print(star*4)
# print(star*5)

# num = 10
# for row in range(1, num+1):
#     print(" "*(num-row), " *"*row)

# string methods
# --------------

# print(dir(name))
name = "ToPS TeCHNolOGy PvT. Ltd."

# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())

# print(name.lower().count('t'))

# print(name.lower().find('t', 1))

star = "*python*"
# print(star.center(9, '-'))
# print(star.center(10, '-'))
# print(star.center(20, '-'))

ingredients = "   ½ to 1 teaspoon green chili  chopped or 1 to 2 green chillies          "

# print(ingredients.rstrip())
# print(ingredients.lstrip())
# print(ingredients.strip())
# print(ingredients.strip().replace("  ", " "))
# print(ingredients.strip().replace(" ", ""))


password = "#@#%^$@"
# print(password.isalpha())
# print(password.isalnum())
# print(password.isdigit())
# print(not password.isalnum())

# print(password.islower())

# print(password.isupper())

# print(password.isspace())

# print(password.startswith("#@#%^$@"))

# print(password.endswith("@"))

# print(password.replace("#@#%^$@", "*"))

# print(password.count("#@#%^$@"))

# password = input("Enter a password: ")

# u = False
# l = False
# d = False
# s = False
# len_ = False

# if len(password) >= 8:
#     len_ = True
#     for ch in password:
#         if ch.isupper():
#             u = True
#         if ch.islower():
#             l = True
#         if ch.isdigit():
#             d = True
#         if not ch.isalnum():
#             s = True

# if len_ and l and u and d and s:
#     print("Valid password")
#     print("Strong password")
#     print("Password strength: Very Strong")
# else:
#     print("Invalid password")
#     if not len_:
#         print("Password should be at least 8 characters long")
#     if not l:
#         print("Password should contain at least one lowercase letter")
#     if not u:
#         print("Password should contain at least one uppercase letter")
#     if not d:
#         print("Password should contain at least one digit")
#     if not s:
#         print("Password should contain at least one special character")


# string formatting
# -----------------
# name = "Python"
# price = 45.677788578
# pages = 300

# print("Book name is: ", name, "Book price is: ", price, "Book total pages : ", pages)

# print(f"Book name is: {name} Book price is: {price} Book total pages : {pages}")

# print("Book name is: {} Book price is: {} Book total pages : {}".format(name, price, pages))

# print("Book name is: {0} Book price is: {1} Book total pages : {2}".format(name, price, pages))

# print("Book name is: %s Book price is: %.2f Book total pages : %d" % (name, price, pages))

# string = input("Enter a string: ").split()
# print(len(string))

# string = "Python Programming"
