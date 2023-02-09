# Classes - Template
# Object - Instance of the class

# DRY - Do not repeat yourself

class student:
    pass


harry = student()
larry = student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]

print(harry.name, larry.std)  # Harry 9
print(larry.subjects)  # ['hindi', 'physics']
print(harry.section, larry.subjects) # 1 ['hindi', 'physics']


