#ex1 Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#ex2 Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#ex3 Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#ex4 Why Use Lambda Functions?
def myfunc(n):
  return lambda a : a * n
#Use that function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)
print(mydoubler(11))
#Or, use the same function definition to make a function that always triples the number you send in:
mytripler = myfunc(3)
print(mytripler(11))