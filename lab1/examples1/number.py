#ex1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#ex2 int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#ex3 float
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

#ex4 complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#ex5 Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#ex6 Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))