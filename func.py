def printinfo(name, age):
    "this prints info into the function"
    print("name: ", name)
    print("age", age)
    return


sum = lambda arg1, arg2 : arg1 + arg2


printinfo(age=50, name="miki")
print("Value of total : ", sum(10, 20))


