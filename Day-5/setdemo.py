# Example1: Creating set
# myset={"apple","banana", "cherry"}
# print(myset)  # unordered list # {'banana', 'apple', 'cherry'} --- we can get result in any of the order

# Example2: Accessing items from set
# myset={"apple","banana", "cherry"}
#
# for i in myset:
#     print(i)    # to print the all value in the sets

# Example3 : Values exists in the set or not
# myset = {"apple", "banana", "cherry"}
#
# print('banana' in myset)  # true
# print('banana1' in myset)  # false

# Example4: adding items to set
# add()- add single items  update()- add mulltiple items

# myset = {"apple", "banana", "cherry"}
# myset.add("orange")   #{'orange', 'apple', 'banana', 'cherry'} -- orange will add on any position
# print(myset)
#
# myset.update(["mango","grapes"])
# print(myset)  # {'grapes', 'apple', 'cherry', 'banana', 'mango'}

# Example5: find numbers of items in a set
# myset = {"apple", "banana", "cherry"}
# print(len(myset)) #3

# Example6: remove items from set - remove() discard()

# - remove()
# myset = {"apple", "banana", "cherry"}
# myset.remove("banana")
# print(myset)     # {'cherry', 'apple'}
# myset.remove("xyz")   #KeyError: 'xyz'

# -discard()
# myset = {"apple", "banana", "cherry"}
# myset.discard("banana")
# print(myset)   # 'apple', 'cherry'}
# myset.discard("xyz")  # will not throw any error

# Example7: clear all the items from the set

# -Clear
# myset = {"apple", "banana", "cherry"}
# myset.clear()
# print(myset)   # set()

# -del
# del myset
# print(myset)  #NameError: name 'myset' is not defined


# Example8: Join the 2 Sets  -union()
# -union()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)  # {1, 2, 3, 'a', 'c', 'b'}

# -update()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)  # {'b', 1, 2, 3, 'c', 'a'}


