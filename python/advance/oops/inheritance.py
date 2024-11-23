#single inh.

# class A:
#     def a(self):
#         print("A's a method")

# class B(A):
#     def b(self):
#         print("B's b method")

# b_obj = B()

# b_obj.a()  # Output: A's a method

# b_obj.b()  # Output: B's b method


# multilevel-inh.

# class A:
#     def a(self):
#         print("A's a method")

# class B(A):
#     def b(self):
#         print("B's b method")

# class C(B):
#     def c(self):
#         print("C's c method")

# c_obj = C()

# c_obj.a()  # Output: A's a method

# c_obj.b()  # Output: B's b method

# c_obj.c()  # Output: C's c method

# multiple-inh.

# class A:
#     def a(self):
#         print("A's a method")

# class B:
#     def b(self):
#         print("B's b method")

# class C(A, B):
#     def c(self):
#         print("C's c method")

# c_obj = C()

# c_obj.a()  # Output: A's a method

# c_obj.b()  # Output: B's b method

# c_obj.c()  # Output: C's c method


#heirarchicle inh.

class A:
    def a(self):
        print("A's a method")

class B1(A):
    def b1(self):
        print("B1's b1 method")

class C1(B1):
    def c1(self):
        print("C1's c1 method")

class C2(B1):
    def c2(self):
        print("C2's c2 method")

class C3(B1):
    def c3(self):
        print("C3's c3 method")

    
class B2(A):
    def b2(self):
        print("B2's b2 method")


obj_c3 = C3()
print(C3.mro())
print(C3.__mro__)

# obj_c3.a()  # Output: C1's c1 method

# obj_c3.b1()  # Output: C2's c2 method

# obj_c3.c3()  # Output: C3's c3 method