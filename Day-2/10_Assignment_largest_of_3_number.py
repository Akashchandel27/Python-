# 3) Check the largest of 3 numbers

a = int(input('Enter the A number'))                # Enter the number a here
b = int(input('Enter the B number'))                # Enter the number b here
c = int(input('Enter the C number'))                # Enter the number c here

if  (a > b) and (a > c):
    print("A is greater")
elif (b > a) and (b > c):
    print("b is greater")
else:
    print("c is greater")
