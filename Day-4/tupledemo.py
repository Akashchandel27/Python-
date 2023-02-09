# Example 1:creating tuple
# mytuple = ('apple', '"banana', 'cherry')
# print(mytuple)

# mytuple = () # Empty Tuple
# print(mytuple)  #()

# Example 2: access tuple items
# mytuple = ('apple', 'banana', 'cherry')
# print(mytuple[1])  # banana      here index starts from 0
# print(mytuple[-1])   #cherry


# Example3: range of indexes
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(mytuple[2:5])  # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])  # ('orange', 'kiwi', 'melon')

# Example 4: changing tuple items
# by default tuple does not allow you change values because it is immutable
# but there is work around
# change the tuple into the list and again change into the tuple
# tuple--> list(modify) --> tuple

# mytuple = ('apple', 'banana', 'cherry')
# print(mytuple)  # here it is print the tuple
#
# mylist = list(mytuple)  # changed to the list
# print(mylist)
#
# mylist[0] = "orange"  # append the value in the list
# print(mylist)  # see.. the changed value here
#
# mytuple = tuple(mylist)  # changed into the tuple again
# print(mytuple)  # see.. the tuple value here

# Example5 : Reading tuple items using loop
# mytuple = ('apple', 'banana', 'cherry')
#
# for i in mytuple:
#     print(i)

# Example6: Check the items Exists (searching of item in tuple)
# mytuple = ('apple', 'banana', 'cherry')
#
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("not present")

# Example7: Tuple length - counting items in a tuple
# mytuple = ('apple', 'banana', 'cherry')
# print(len(mytuple)) #3

# Example8: Add items to tuples
# Not possible because tuple is immutable- can't change values/items
# mytuple = ('apple', 'banana', 'cherry')
# mytuple[0]="orange"
# print(mytuple)   #'TypeError: tuple' object does not support item assignment

# Example9: copy tuple
# mytuple1 = ("apple", "banana", "cherry")
# mytuple2=mytuple1
# print(mytuple2)    #('apple', 'banana', 'cherry')

# Example10: removing items from tuple not possible bcoz tuple is immutable
# mytuple=("apple", "banana", "cherry")
# mytuple.remove("apple") # invalid /it is not possible
# del mytuple
# print (mytuple)  #NomeError: nome 'mytuple' is not defined

# Example11: Join/combine tuple

# tuple1 = (10, 20, 30)
# tuple2 = ('a', 'b', 'c')
#
# tuple3 = tuple1 + tuple2
# print(tuple3)

# Example12:
# tuple1=(10,20,30)
# tuple2 = ('a', 'b', 'c')
#
# if tuple1==tuple2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")

akash = ["akash","chandel",29]

print(type(akash))

chinu = tuple(akash)

print(type(chinu))

