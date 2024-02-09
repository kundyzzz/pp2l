#ex1 Create a Class
class MyClass:
  x = 5

#ex2 Create Object
p1 = MyClass()
print(p1.x)

#ex3 The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#ex4 The __str__() Function
#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)
#The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

#ex5 Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#ex6 The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

#ex7 Modify Object Properties
#Set the age of p1 to 40:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

#ex8 Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)

#ex9 Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)

#ex10 The pass Statement
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement
