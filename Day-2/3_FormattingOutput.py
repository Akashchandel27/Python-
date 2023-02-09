name = "john"
age = 300
sal = 5000.50

# print(name)
# print(age)
# print(sal)
#
# # Other to write the same is:-
# name, age, sal = "john", 30, 5000.50
# print(age, sal, name)
#
# print(sal)
# print(name, age)

# Approach2

# Name is: john
# Age is: 30
# Sal is: 5000.5

# print("Name is:", name)
#
# print("Age is:", age)
# print("Sal is:", sal)

# Approach3
print("Name is:%s Age is: %d Salary is: %i" % (name,age,sal))

# Approach4
print("Name is: {} Age is:{} Salary is: {}".format(age, age, sal))
print("Age is:{} Name is: {} Salary is: {}".format(name, age, sal))
