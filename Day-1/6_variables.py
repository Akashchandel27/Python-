a = 10
b = 20
s = 'welcome'

print(type(a))  # class int
print(type(b))  # class int
print(type(s))  # class str

#################### Example 1 ###############

a = 10
b = 10.5
print(a)  # 10
print(b)  # 10.5
print(a, b)  # 10 10.5

#################### Example2 ######################

a = 10
b = 20
c = 'welcome'

a, b, c = 10, 20, 'welcome'
print(a+b, c)  # 10 20 welcome

# it is join the same data type

#################### Example3  ######################

a = b = c = 100
print(a + 1, b + 2, c * 7)  # 101 102 700

#################### Example4  ######################
x = 1
y = 2
print(x, y)  # 1 2
x, y = y, x

print(x, y)  # 2 1
