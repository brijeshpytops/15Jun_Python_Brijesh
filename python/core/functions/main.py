"""
syntax:
def function_name():
    # code block

function call:
function_name()
"""

# def greet():
#     print("Hello, World!")

# greet()

# def greet(name):
#     print(f"Hello, {name}!")
#     print("Welcome to Python!")

# greet(input("Enter your name: "))

# types of parameter
# positional
# def add(a, b):
#     print(a + b)

# add(10, 20)
# def add(a, b, c):
#     print(a + b + c)

# add(10, 20, 30)

# default/keyword parameter

# def bill(tomato, potato=100):
#     print("Total = ", tomato + potato)

# bill(50, 30)

# variable length parameter
# *args
# **kwargs

# def add(*nums):
#     # print(type(nums))
#     print(sum(nums))

# add(653, 4567, 23, 7, 384, 678446)


# def bill(**products):
#     # print(type(products))
#     total = 0
#     for item, price in products.items():
#         print(f"{item} : {price}")
#         total += price
#     print("-"*40)
#     print("Total amount: ", total)
#     # GST 5% apply
#     print("GST: ", total * 0.05)
#     print("Final amount: ", total + (total * 0.05))

# bill(pen=100, book=30, milk=33)

# lambda function
# addition = lambda num1, num2: num1 * num2

# print(addition(20, 40))

# map function
# print(list(map(lambda num:num*num, [1,2,3,4,5,6,7,8,9,10])))

# def getEvenNums(num):
#     if num % 2 == 0:
#         return num

# print(list(filter(getEvenNums, [1,2,3,4,5,6,7,8,9,10])))

# def check_length(func):
#     def wrapper():
#         res = func()
#         if len(res) >= 8:
#             return True
#         else:
#             return False
#     return wrapper

# def title_case(yoyo):
#     def inner():
#         res = yoyo()
#         return res.title()
#     return inner

# @check_length
# @title_case
# def text():
#     return input("Enter something... ")

# print(text())

# x = 20 # global variable

# def text():
#     global x
#     x = 10 # local variable
#     print(x)

# text()
# print(x)

# def outer():
#     def inner():
#         return "I am from inner function"
#     return inner

# func = outer()

# print(func())

def calc():
    a = 10
    b = 20

    return a+b, a-b, a*b, a/b

# result = calc()
# print(result)
add, sub, mul, div = calc()

print(f"Addition: {add}")

print(f"Subtraction: {sub}")

print(f"Multiplication: {mul}")

print(f"Division: {div}")
