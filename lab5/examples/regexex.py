import re

#ex1 Check if the string starts with "The" and ends with "Spain":      f search

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#ex2 Make a search that returns no match:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)    #no match

#ex3 Print a list of all matches:          f findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)   #['ai','ai']

#ex4 Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)  #[] no match

#ex5 Split at each white-space character:      f split
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)    #['The', 'rain', 'in', 'Spain']

#ex6 Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)    #['The', 'rain in Spain']

#ex7 Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)    #The9rain9in9Spain

#ex8 Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)    #The9rain9in Spain

