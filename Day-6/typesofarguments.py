# Example1:

# def func(i,j):
#     print(i,j)
#
# func(10,20)  # Positional arguments #10 20
#
# func(j=200,i=10)  #keyword arguments #10 200

# Example 2:-
# def func(i,j=10):
#     print(i,j)
#
# # func(100,200)  # Positional arguments # 100 200
# func(100)  # Positional arguments     #100,10

# Example 3:- #keyword arguments
# def greeting(name,greetmsg):
#     print(greetmsg+" "+name + " " + "india")
#
# greeting(name='john',greetmsg='hello')  #hello john
# greeting(greetmsg='hello',name='john')  #hello john

# Example 4:- #Postional and keywords arguments
# def my_func(a, b, c):
#     print(a, b, c)


# my_func(10,20,30)  # Positional arguments #10 20 30
# my_func(a=10, b=20, c=40) #keyword arguments #10 20 40

# my_func(10,20,c=30)  # 10 20 30
# my_func(10,b=20,c=30) #10 20 30
# my_func(10,b=20,30)   # Positional argument after keyword argument
# my_func(10,30,b=20)   #this is having logical error

# Example 5:- function can return multiple values

# def largest(a,b):
#     if a>b:
#         return a,b
#     else:
#         return b,a
#
# # print(largest(100,200)) #(200, 100)
# # print(largest(30,200))  #(200, 30)
#
# res=largest(10,20)
# print(res)               # (20, 10)
#
# print(type(res))  # <class 'tuple'>


