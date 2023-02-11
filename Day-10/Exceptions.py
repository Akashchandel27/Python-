#Example-1

# print("thhis is starting point of prpgram")
# print("thhis is starting point of prpgram")
# print("thhis is starting point of prpgram")
# try:
#     print(x)
# except:
#     print("expection occured")
#
# print("end of the program")
# print("end of the program")
# print("end of the program")

#Example:-2

# print("this is starting point of prpgram")
#
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("expection handled ")
#
# print("end of the program")

#Example:-3 Multiple expect blocks - try,except  else finally

#
# try:
#     num1,num2 = 10,2
#     result= num1/num2
#     print("result is", result)
#
# except ZeroDivisionError:
#     print("Thrown zerodivision error" )
# except SyntaxError:
#     print("other expection")
# except:
#     print("error")
#
# else:
#     print("No expection occured")
#
# finally:
#     print("always excuated ")

#Example:-4 raising our own expections

# def enterage(num):
#     if num<0:
#         raise ValueError("only interger are allowed")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#
# print("checking the number is even or odd")
#
# num=-1
# try:
#     enterage(num)
#
# except ValueError:
#     print("value error expection occured and handled")
#
# print("program overed")