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

# class A:  # parent
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
# class B: # parent
#     a,b =200,100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A,B): # child
#     i, j = 5, 3
#
#     def m3(self):
#         print(self.i * self.j)
#
# mc1=C()
# mc1.m1()
# mc1.m2()
# mc1.m3()

# Example:6 ( calling parent class method using child class super()

# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m1(self):
#         print("this is m1 method from class b")
#         super().m1()
#
# mc1=B()    #Overriding methods
# mc1.m1()  #"this is m1 method from class b")
#
#
# # Super() is the class which is in the child class and calling the parent functions
#
# #if we want to invoke the parent class

# Example:7

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)     #local variable
#         print(self.i +self.j)
#         print(self.a+self.b)
#
# mc1=B()
# mc1.m(1000,2000)


# Example 8:- Overriding variable

# class Parent:
#     name="scott"
#
# class Child(Parent):
#     name="john"    #overriding the variable value
#     def test(self):
#         print(super().name)
#
# mc1=Child()
# print(mc1.name)
# mc1.test()

# Example 9: Overriding methods

# class Bank:
#     def rateofInterest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateofInterest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateofInterest(self):
#         return 12
#
# objx = XBank()
# print(objx.rateofInterest())    #10
#
# objy = YBank()
# print(objy.rateofInterest())    #12


#Example 10:- Overloading concept (polymorphism)

# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("hello " +name)
#         else:
#             print("No helo")
#
#
# h=Human()
# h.sayhello("scott")
# h.sayhello()

#Example 11:- Overloading 2

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add()              #0
calobj.add(10)            #10
calobj.add(10,20)         #30
calobj.add(10,20,30)      #60
