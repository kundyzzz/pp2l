#ex1 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#ex2 Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#ex3 Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#ex4 Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#ex5 The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#ex6 The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#ex7 
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#ex8
def myFunction() :
  return True
print(myFunction())

#ex9 
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

#ex10 Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
