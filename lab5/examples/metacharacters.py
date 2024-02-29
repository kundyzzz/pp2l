import re
txt = "The rain in Spain"

#ex1 []	A set of characters
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)    #['h', 'e', 'a', 'i', 'i', 'a', 'i']

#ex2 \	Signals a special sequence 
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)    #['5', '9']

#ex3 .	Any character (except newline character)
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)    #['hello']

#ex4 ^	Starts with
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")     #Yes, the string starts with 'hello'

#ex5 $	Ends with 
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")     #Yes, the string ends with 'planet'

#ex6 *	Zero or more occurrences 
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)    #['hello']

#ex7 ?	Zero or one occurrences
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)    #[]

#ex8 {}	Exactly the specified number of occurrences
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)    #['hello']

#ex9 |	Either or
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")     #['falls]