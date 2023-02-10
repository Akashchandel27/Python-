# Example1

# class A:   # parent
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A): #child
#     def m2(self):
#         print("this is m2 method from class B")
#
# # mc1=B()  # calling the class B ( we can call both m1 and m2 method)
# # mc1.m1()
# # mc1.m2()
#
# mc1=A()  # error we will get as we can't call m2
# mc1.m1()
# mc1.m2()

# Example:2 :Single Inheritance

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x +self.y)
#
# class B(A):
#     a,b=100,200
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# mc1=B()
# mc1.m1()  # 30
# mc1.m2()  # -100

# Example-3 Multi-level inheritance

# class A:  # Grand parent
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A): # parent
#     a,b =200,100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B): # child
#     i, j = 5, 3
#
#     def m3(self):
#         print(self.i * self.j)
#
# mc1=C()
# mc1.m1()
# mc1.m2()
# mc1.m3()

# Example:-4

# class A:  # parent
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A): # child
#     a,b =200,100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A): # child
#     i, j = 5, 3
#
#     def m3(self):
#         print(self.i * self.j)
#
# mc1=C()
# mc1.m1()
# mc1.m3()   # Can't access m2
#
# mc2=B()
# mc2.m1()
# mc2.m2()   # Can't access m3

# Example:5 Multiple Inheritance

class A:  # parent
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)

class B: # parent
    a,b =200,100

    def m2(self):
        print(self.a - self.b)


class C(A,B): # child
    i, j = 5, 3

    def m3(self):
        print(self.i * self.j)

mc1=C()
mc1.m1()
mc1.m2()
mc1.m3()





