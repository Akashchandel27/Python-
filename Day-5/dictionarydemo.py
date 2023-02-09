# Example1 : creating dictionary
# mydic1={101:"x",102:"y",103:"z",102:"x"}
# print(mydic1) #{101: 'x', 102: 'y', 103: 'z'}

# Example2 : access items from dictionary
#
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2021,
#
#
# }
#
# print(mydic["year"])
# print(mydic["brand"])  #Hyundai
# print(mydic["model"])  #110

# using get()
# x=mydic.get("brand")
# print(mydic.get("brand"))  #Hyundai
# print(x)

#Example3: Changes values in dictionary

# mydic1 = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2021
# }
#
# mydic1["year"]=2050
#
# print(mydic1)



# Example4 : reading items from dictinoary using loop
# mydic = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# for i in mydic:
#     print(i)   # prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i]) # prints only values from dictionary
#
# for i in mydic.values():
#     print(i)   # prints only values from dictionary
#
# for x,y in mydic.items():
#     print(x,y) # print keys along with the values

# Example5: check keys is exist in dictionary or not
# mydic = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# if "model" in mydic:    # only the keys values it will search
#     print("exist")    #true
# else:
#     print("not exist")
#
# print("model" in mydic)

# Example6:find number if items in dictionary
# mydic = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# print(len(mydic))   #3

# Example7: Adding items to dictionary
# mydic = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# mydic["color"]="red"
# print(mydic)  #{'brand': 'Hyundai', 'model': '110', 'year': 2020, 'color': 'red'}

# Example8: remove items from dictionary
# mydic = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }

# -pop
# mydic.pop("year")
# print(mydic) #{'brand': 'Hyundai', 'model': '110'}

# del mydic['year']
# print(mydic) #{'brand': 'Hyundai', 'model': '110'}

# del mydic   # delete all here
# print(mydic)  #ameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic)   #{}

# Example 9: copying dictionary
# mydic1 = {
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# using copy()
# mydic2=mydic1.copy()
# print(mydic1) #{'brand': 'Hyundai', 'model': '110', 'year': 2020}

# #without using copy()
# mydic2=mydic1
# print(mydic2) #{'brand': 'Hyundai', 'model': '110', 'year': 2020}


