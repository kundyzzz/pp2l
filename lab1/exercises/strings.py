#ex1 Use the len function to print the length of the string.
x = "Hello World"
print(len(x))   #9

#ex2 Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
print(x)     #H

#ex3 Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)    #llo

#ex4 Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
print(txt.strip())    #Hello World

#ex5 Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
print(txt)      #HELLO WORLD

#ex6 Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()       #hello world

#ex7 Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H","J")      #Jello World

#ex8 Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))      #My name is john, and I am 36
