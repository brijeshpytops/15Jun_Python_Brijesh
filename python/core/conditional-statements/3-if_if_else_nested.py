"""
nested conditions in python?

Syntax:

if condition1:
    if condition2:
        statement1
    
if condition1:
    if condition2:
        statement1
    else:
        statement2
else:
    statement3

"""

# Example: 

# x = 5
# if x > 3:
#     if x < 10:
#         print("x is greater than 3 and less than 10")
#     else:
#         print("x is greater than 3 but not less than 10")
# else:
#     print("x is not greater than 3")

# Example: 

age = int(input("Enter your age: "))
if age >= 18:
    weight = float(input("Enter your weight: "))
    if weight >= 50:
        print("You are eligible for blood donate.")
    else:
        print("You are not eligible for blood donate.")
else:
    print("You are not eligible for blood donate.")
