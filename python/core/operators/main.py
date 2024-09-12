"""
What is operators and oprands in python?

Operators are special symbols used to perform operations on operands.

Example:
a = 10
b = 20
c = a + b

here a, b, c - operands
    +,= - operators

Here are some commonly used operators in Python:
    - Arithmetic operators (+, -, *, /, //, %, **)
    - Assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
    - Comparison operators (==, !=, <, >, <=, >=)
    - Logical operators (and, or, not)
    - Bitwise operators (&, |, ^, ~, <<, >>)
    - Membership operators (in, not in)
    - Identity operators (is, is not)
"""

# Note: Python supports operator overloading, which allows defining custom behavior for operators on user-defined types.

# Examples:

# Arithmetic operators
# a = 10
# b = 20
# print(a + b)  # Output: 30
# print(a - b)  # Output: -10
# print(a * b)  # Output: 200
# print(a / b)  # Output: 0.5

# # Floor division operator

# print(a // b)  # Output: 0

# # Modulus operator

# print(a % b)  # Output: 10

# # Exponentiation operator

# print(a ** b)  # Output: 100000

# Assignment operators

a = 10
b = 20

# a += b  # Output: 30
# a -= b  # Output: -10

# # a *= b  # Output: 200

# # a /= b  # Output: 0.5

# # Floor division operator

# a //= b  # Output: 0

# # Modulus operator

# a %= b  # Output: 10

# # Exponentiation operator

# a **= b  # Output: 100000

# Comparison operators

# a = 10

# b = 20

print(a < b) # True

print(a <= b) # True

print(a > b) # False

print(a >= b) # False

print(a == b) # False

print(a!= b) # True

# Logical operators

a = True

b = False

print(a and b)  # Output: False

print(a or b)  # Output: True

print(not a)  # Output: False

# Membership operators

my_list = [1, 2, 3, 4, 5]

print(1 in my_list)  # Output: True

print(6 in my_list)  # Output: False

print(6 not in my_list) # Output: True

code = "Python"

print("P" in code) # True
print("P" not in code) # False
print("to" not in code) # True
print("tho" not in code) # False
print("toh" not in code) # True
print("p" not in code) # True

# Identity operators

a = 10

b = 10

print(a is b)  # Output: True

a = "Hello"

b = "Hello"

print(id(a))
print(id(b))

print(a is b)  # Output: True

a = [1, 2, 3]

b = [1, 2, 3]

print(a is b)  # Output: False

print(id(a))
print(id(b))
# Note: The "is" operator checks for object identity, not value equality. If you want to check if two variables point to the same object, use "==" operator.

# Examples:

# a = 10

# b = 10

print(a is not b)  # Output: False

# Bitwise operators 

# & (AND) - Returns 1 if both bits are 1, else 0

# | (OR) - Returns 1 if at least one of the bits is 1, else 0

# ^ (XOR) - Returns 1 if the bits are different, else 0

# ~ (NOT) - Returns 1 if the bit is 0, else 0

# << (LEFT SHIFT) - Shifts the bits of the number to the left by the specified number of places

# >> (RIGHT SHIFT) - Shifts the bits of the number to the right by the specified number of places


# Example:

a = 3
b = 5

print(a & b)  # Output: 1

print(a | b)  # Output: 7

print(a ^ b)  # Output: 6

print(~a)  # Output: -4


a = 7

a = a << 2
print(a) # Output: 28

print(a << 3) # Output: 224