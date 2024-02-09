#ex1 creating a function
def my_function():
  print("Hello from a function")

#ex2 Calling a Function
def my_function():
  print("Hello from a function")
my_function()

#ex3 Arguments
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#ex4 Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#ex5 Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#ex6 Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#ex7 Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#ex8 Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#ex9 Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#ex10 Return Values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#ex11 The pass Statement
def myfunction():
  pass

#ex12 Positional-Only Arguments
def my_function(x, /):  #1
  print(x)
my_function(3)

def my_function(x):     #2
  print(x)
my_function(x = 3)

def my_function(x, /):  #3 ERROR
  print(x)
my_function(x = 3)

#ex13 Keyword-Only Arguments
def my_function(*, x):      #1
  print(x)
my_function(x = 3)

def my_function(x):         #2
  print(x)
my_function(3)

def my_function(*, x):      #3 ERROR   
  print(x)
my_function(3)

#ex14 Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

#ex15 Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)