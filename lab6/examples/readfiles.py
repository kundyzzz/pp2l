#ex1 
f = open("demofile.txt", "r")
print(f.read())

#ex2 Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))    #Return the 5 first characters of the file:

#ex3 Read Lines
f = open("demofile.txt", "r")
print(f.readline())

#ex4 
f = open("demofile.txt", "r")
for x in f:
  print(x)

#ex5 Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()
