# Example1:- how to create the class and object

# class Myclass:                       # to create class inside the variable and methode
#     def myfun(self):
#         pass
#
#     def display(self,name):
#         print(name)
#
#     def display1(self,l_name):
#         print(l_name)
#
# mc1=Myclass()  # call through the object name
# mc1.myfun()
# mc1.display("akash")
# mc1.display1("chandel")


# Example2 :-

# class MyClass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,num):
#         print(num)
#
# mc=MyClass()
# mc.m1()
# mc.m2(100)  # mc.m2(100)  error we get here

#Example 3:-

# class MyClass:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,num):
#         print(num)
#
# mc=MyClass()
# mc.m1()
# mc.m2(12,100)  # mc.m2(100) self is consider as a parameter
#
# MyClass.m2(12,23) # here calling the static method directly using the class not through the object


#Example 4:-

# class Myclass:
#     a,b = 10,20  #class variable
#
#     def add(self):
#         print(self.a+self.b)
#
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()
# mc.mul()


#Example 5:-

# i,j =20,98                                     #global variable
#
# class Myclass:
#     a,b =10,20                                 #class variable
#
#     def add(self,x,y):                         # x and y are the local variable
#         print(self.a+self.b)    # a,b are the class variable printed
#         print(i+j)              # i, j are global varible printed
#         print(x+y)              # x, y are the local variable
#
# mc=Myclass()
# mc.add(100,2300)


#Example 6:- once class can have multiple object

# class Myclass:
#     def display(self,name):
#         print("this is display method")
#         print(name)
#
# obj1=Myclass()
# obj1.display("akash")
#
# obj2=Myclass()
# obj2.display("CHANDEL")


#Example 7:-  Constructor example

# class Myclass:
#     def __init__(self):
#         print("this is constructor")
#     def m1(self):
#         print("hello")
#
# Myclass()  #invoke the constructor automatically
#
# mc =Myclass()
# mc.m1()

# Example:-8

# class Myclass:
#     name="john"
#     def __init__(self,name): # constructor expecting  one argument
#         print(name)
#         print(self.name)
#
# Myclass("akash")  # passing parameter to the constructor

# Example:-9

# Reg:- EMP
# Constuctor : eid, name , sal
# display : print eid.ename & sal

# class Emp:
#
#     def __init__(self,eid,name,sal):
#         self.eid=eid
#         self.name=name
#         self.sal=sal
#
#     def display(self):
#         print(self.eid,self.name,self.sal)
#
#
# e1=Emp(101,"john",23999)
# e1.display()
#
#
# e2=Emp(102,"johnnt",2399)
# e2.display()
#
#
# Example:10
class Emp:

    def __init__(self,eid,name,sal):
        self.eid=eid
        self.name=name
        self.sal=sal

    def __str__(self): # it is the string constuctor will return only the string value
        return (self.name)
        # return (Selg.name,self.sal)  invalid


e1=Emp(101,"john",23999)
print(e1)

e2=Emp(102,"johnnt",2399)
print(e2)




















