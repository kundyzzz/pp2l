#ex1 
print("Hello")
print('Hello')

#ex2 You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ex3
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#ex4 Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#ex5 Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#ex6 The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#ex7 Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#ex8 Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#ex9 Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#ex10 print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")