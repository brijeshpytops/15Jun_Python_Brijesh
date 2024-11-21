"""
syntax of class :

class ClassName:
    # class body
    # data member [attribute and property]
    # methods [functions and behaviors]

syntax of object :

object_name = ClassName()

"""

# name = "brijesh"
# age = 28

# def run():
#     print("Running...")

# print(name)
# print(age)
# run()

# class Person:
#     name = "brijesh"
#     age = 28

#     def run(self):
#         print("Running...")

# obj = Person()
# # print(dir(obj))

# print(obj.name)
# print(obj.age)
# obj.run()
# # print(type(obj))

# class Person:
#     # constructor
#     def __init__(self, name, age):
#         self.name_ = name
#         self.age_ = age
#         self.speed_ = r'10km\h'

#     def display(self):
#         print(f"Name: {self.name_}, Age: {self.age_}, Speed: {self.speed_}")

# # b = Person("brijesh", 28)
# # b.display()

# # j = Person("Jay", 27)
# # j.display()

# while(True):
#     obj = Person(input("Enter a name :"), input("Enter a age: "))
#     obj.display()

class Tops:
    class Students:
        pass
    class Employee:
        # constructor
        def __init__(self, name, age):
            self.name_ = name
            self.age_ = age
            self.salary = 10000

        def display(self):
            print(f"Name: {self.name_}, Age: {self.age_}, Salary: {self.salary}")

brijesh = Tops().Employee("brijesh", 28)
brijesh.display()
jay = Tops().Employee("jay", 28)
jay.display()