#ex1 Save this code in a file named mymodule.py
# def greeting(name):
#   print("Hello, " + name)

# #ex2 Import the module named mymodule, and call the greeting function:
# import mymodule
# mymodule.greeting("Jonathan")

# #ex3 Save this code in the file mymodule.py
# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# #Import the module named mymodule, and access the person1 dictionary:
# import mymodule
# a = mymodule.person1["age"]
# print(a)

# #ex4 Create an alias for mymodule called mx:
# import mymodule as mx
# a = mx.person1["age"]
# print(a)

# #ex5 Import and use the platform module:
# import platform
# x = platform.system()
# print(x)

# #ex6 List all the defined names belonging to the platform module:
# import platform
# x = dir(platform)
# print(x)

# #ex7 The module named mymodule has one function and one dictionary:
# def greeting(name):
#   print("Hello, " + name)

# person1 = {
#   "name": "John",
#   "age": 36,
#   "country": "Norway"
# }
# #Import only the person1 dictionary from the module:
# from mymodule import person1
# print (person1["age"])
