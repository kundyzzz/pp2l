#ex1 Delete a File
import os
os.remove("demofile.txt")

#ex2 Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#ex3 Delete Folder
#os.rmdir("myfolder")
