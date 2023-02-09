# Example1: how to create list

# mylist1=[10,20,30,40,58]
# mylist2=["apple", "banana", "cherry"]
# mylist3=["apple",10, "banana", 20]
# #mylist=list[] # empty list
#
# print (mylist1)
# print (mylist2)
# print (mylist3)
# #print(mylist)

# Example2: Accessing items from the list
# mylist = ["apple", "banana", "cherry"]  # index starts from 0

# print(mylist[0])  # apple
# print(mylist[2])  # cherry
# print(mylist[-1])  # cherry
# print(mylist[-2])  # banana

# Example3: Range of indexes
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5])    # ['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])  # ['orange', 'kiwi', 'melon']

# Example4: change item value
# mylist = ["apple", "banana", "cherry"]
# print(mylist)         # ['apple', 'banana', 'cherry']
# mylist[0] = "orange"  # this will change the values based on index
# print(mylist)         # ['orange', 'banana', 'cherry']

# Example5: read the list items using loop
# mylist = ["apple", "banana", "cherry"]
#
# for i in mylist:
#     print(i)

# Example6: check if the item is existed in the list or not
# mylist = ["apple", "banana", "cherry"]
#
# if "apple" in mylist:
#     print('yes, apple is present')
# else:
#     print("no, apple is not present")

# Example7: List length (Count number if items in a list)
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))  #3

#Example 8: Add items in the list append() insert()
# mylist = ["apple","banana","cherry"]
# # mylist.append("orange")        #adding new items at the end of the list
# # print(mylist)                  # ['apple', 'banana', 'cherry', 'orange']
#
# mylist.insert(1,"orange")  #adding where ever you want to add in the list
# print(mylist)          # ['apple', 'orange', 'banana', 'cherry']

# Example9 : Remove the items from the list
# 1) pop()
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)  # here we should specify index not the value
# print(mylist)  # ['banana', 'cherry']

# 2) del()
# mylist = ["apple", "banana", "cherry"]
# del mylist[2]    # here del command remove single items based on the index
# print(mylist)    #['apple', 'banana']

# 3) clear()
# mylist = ["apple", "banana", "cherry"]
# mylist.clear()   #to clear all the items in the list
# print(mylist)  #[]

# Example 10: Copy list
# list()
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = list(mylist1)
#
# print(mylist1) #['apple', 'banana', 'cherry']
# print(mylist2) #['apple', 'banana', 'cherry']

# copy()
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = mylist1.copy()
# print(mylist1)  # ['apple', 'banana', 'cherry']
# print(mylist2)  # ['apple', 'banana', 'cherry']

# Example11: Join/combine list
# using + operator
# list1 = ['a', "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# using loop statements
# list1 = ['a', "b", "c"]
# list2 = [1, 2, 3]
#
# print(list1+list2)

# for i in list2:
#     list1.append(i)

# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# using the extend()
# list1 = ['a', "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)   # ['a', 'b', 'c', 1, 2, 3]

# Example12:
# list1 = [10, 20, 30]
# list2 = ['a', 'b', 'c']
#
# if list1 == list2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")
