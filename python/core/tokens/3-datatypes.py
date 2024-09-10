"""
What is datatypes in python?

Python has several built-in data types that can be used to store and manipulate information. Some of the commonly used data types are:
    - Integers (e.g., 1, 2, 3)
    - Floating-point numbers (e.g., 1.2, 3.5)
    - Complex numbers (e.g., 1+2j, 3+4j)
    - Strings (e.g., "Hello", "World")
    - Booleans (e.g., True, False)
    - Lists (e.g., [1, 2, 3], ["a", "b", "c"])
    - Tuples (e.g., (1, 2, 3), ("a", "b", "c"))
    - Sets (e.g., {1, 2, 3}, {"a", "b", "c"})
    - Dictionaries (e.g., {"name": "John", "age": 30}, {"fruit": "apple", "color": "red"})
    - None (e.g., None)
    - Custom data types (e.g., custom classes)

"""
age = 34
print(type(age)) # <class 'int'>

float_num = 3.14

print(type(float_num)) # <class 'float'>

complex_num = 2 + 3j

print(type(complex_num)) # <class 'complex'>

string = "Hello World"

print(type(string)) # <class 'str'>

boolean = True

print(type(boolean)) # <class 'bool'>

list_of_numbers = [1, 2, 3]

print(type(list_of_numbers)) # <class 'list'>

tuple_of_numbers = (1, 2, 3)

print(type(tuple_of_numbers)) # <class 'tuple'>

set_of_numbers = {1, 2, 3}

print(type(set_of_numbers)) # <class 'set'>

dictionary_of_names_ages = {"John": 30, "Alice": 28}

print(type(dictionary_of_names_ages)) # <class 'dict'>

none_value = None

print(type(none_value)) # <class 'NoneType'>

# Custom data types

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(type(person)) # <class '__main__.Person'>