# create string variable

# Example 1 : ways of creating string variables
# s="welcome"
# s='welcome
# s=str('welcome')
# s=str("welcome")

# creating empty string variable
# name=str()
# name=""
# name=''

# Example 2 : ways of creating string variables
# mutable- cannot change the value of variable
# immutable - can change the value of variable

# string is immutable?
# if the value is changed after update then it is immutable

# str1 = "welcome"
# print(id(str1))  # 2984541559472
# str1 = str1 + "to python"
# print(id(str1))  # 1638475397872

# if the values is changed after updation, then it is immutable

# Example 3 : + and * with string
# str="welcome"
# print(str+"programming")            # concatenation/joining
# print(str*3)                        #welcomewelcomewelcome

# Example4 slicing []
# starting index 0
# ending index 1

# str = "welcome"
# print(str[1:3])           # el
# print(str[:6])            # welcom here starting index is by default
# print(str[2:])            # lcome

# print(str[1:-1])          # elcom last 1 char removed
# print(str[1:-2])          # elco last 2 char removed

# Example5 ord() and chr()
# print (ord('A'))           #65 # returns the ASCII code of the character.
# print (chr(65))            #A #returns character represented by a ASCII number.

# Example6: max() min() len()
# Compare with the ASCII Tables
# print(max("abc"))  # c
# print(min("abc"))  # a
# print(len("abc"))  # 3

# Example 7: in, not in operators returns true/false
# s = "welcome"
# print("come" in s)  # True
# print("lome" in s)  # False

# print("come" not in s)  # False
# print("lome" not in s)  # True

# Example 8: String comparison
# print("tim" == "tie")  # False
# print("free" != "freedom")  # True
# print("arrow" > "aron")  # True
# print("right" >= "left")  # True
# print("teeth" < "tee")  # False
# print("yellow" <= "fellow")  # False
# print("abc" > "")  # True

#Example9 : Testing strings True/False
# s = "welcome to python"
# print(s.isalnum())          # False  ------check the string contains the numbers or not??
#
# print("Welcome".isalpha())  # True..
# print("2012".isdigit())     # True
# print("first Number".isidentifier())  # False
# print(s.islower())           # True
# print("WELCOME".isupper())   # True
# print(" ".isspace())         # True

# Example 10: Searching for Substrings
# s = "welcome to python"
# print(s.endswith("thon"))  # True
# print(s.startswith("good"))  # False
#
# print(s.find("come"))  # 3
# print(s.find("become"))  # -1 not found
# print(s.count("t"))  # 2 #Returns number of occurrences of substring the string

# Example11: Converting String
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)  # String in python
#
# s2 = s.title()
# print(s2)  # String In Python
#
# s3 = s.lower()
# print(s3)  # string in python
#
# s4 = s.upper()
# print(s4)  # STRING IN PYTHON
#
# s5 = s.swapcase()
# print(s5)  # STRING IN python
#
# s6 = s.replace("in", "on")
# print(s6)  # String on PYTHON

# Example12: Reverse a string

# Method1
# s = "welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str
# print("reversed string is:", rev_str)  # emoclen

# Method2
# s = "welcome"
# rev_str = s[::-1]  # s[8:7:-1]
# print(rev_str)  # emoclew
