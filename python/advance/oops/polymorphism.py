# class Maths:
#     def add(self, num1, num2):
#         return num1 + num2
    
#     def add(self, num1, num2, num3):
#         return num1 + num2 + num3
    
# obj = Maths()
# print(obj.add(10, 20)) # TypeError: Maths.add() missing 1 required positional argument: 'num3'

# x  = 10
# x = 20
# print(x)


# class Maths:
#     def add(self, num1=None, num2=None, num3=None):
#         if num1 != None and num2 != None and num3 != None:
#             return num1 + num2 + num3
#         elif num1 != None and num2 != None:
#             return num1 + num2
        

# obj = Maths()
# print(obj.add(10, 20))
# print(obj.add(10, 20, 40))
# print(obj.add(10, 20, 40, 50))

# class Maths:
#     def add(self, *nums):
#         total = 0
#         for num in nums:
#             total += num
#         return total
    
# obj = Maths()
# print(obj.add(10, 20))
# print(obj.add(10, 20, 30))
# print(obj.add(10, 20, 30, 40))
# print(obj.add(10, 20, 30, 40, 50))

# class Maths:
#     def add(self, **nums):
#         total = 0
#         for key, num in nums.items():
#             total += num
#         return total
    
# obj = Maths()
# print(obj.add(num1=10, num2=20))
# print(obj.add(num1=10, num2=20, num3=30))
# print(obj.add(num1=10, num2=20, num3=30, num4=40))
# print(obj.add(num1=10, num2=20, num3=30, num4=40, num5=50))

# def test(name=None):
#     print(name)

# test(name="brijesh")


# class Math1:
#     def info(self):
#         return "this is a parent method"
    
# class Math2(Math1):
#     def info(self):
#         print(super().info())
#         return "this is a child method"
    
# obj = Math2()
# # print(dir(obj))
# print(obj.info())
