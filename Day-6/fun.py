xy = 100  # global variable

def cool():
    # global xy=200    #invalid syntax
    global xy        #Here, we are access the value of global variable
    xy = 200         #local variable
    print(xy)        #local variable values is printed

cool()  #200

print(xy)

def cool2():
    # global xy=200    #invalid syntax
    global xy        #Here, we are access the value of global variable
    xy = 2000         #local variable
    print(xy)        #local variable values is printed

cool2()

print(xy)


