#ex1 Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex2 Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#ex3 Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#ex3 Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex4 Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#ex5 Using the range() function:
for x in range(6):
  print(x)

#ex6 Using the start parameter:
for x in range(2, 6):
  print(x)
