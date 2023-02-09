# Example1:-
# global_var = 20  # global variable

# def func():
#     local_var = 10  # local variable
#     print(local_var)  # 10
#     print(global_var)  # 20
#
# func()
#
# # print(local_var) #invalid because local_var is local variable of func()
# print(global_var)  # valid because global_var is having global variable

# Example2:-
# xy = 100  # global variable
#
# def cool():
#     # global xy=200    #invalid syntax
#     global xy        #Here, we are access the value of global variable
#     xy = 200         #local variable
#     print(xy)        #local variable values is printed
#
# cool()  #200
#
# print(xy)  # global xy we have changed the values and it will permentat changed the value for that variable

# Example3:- Global variable is changed
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x) #500
#
# cool()
#
# print(x)  #500

# Example4:- Global variable is changed
# x=100
#
# def cool():
#     x=500
#     print(x) #500
#
# cool()
#
# print(x)  #100

# Example5:-
# we can delcare the  Global variable is created inside the function also -- just we need to give global keywords before the variable
# def cool():
#     global x
#     x=100
#     print(x)  #100
# cool()

# print(x)    #100 #able to access x because it is global variable

