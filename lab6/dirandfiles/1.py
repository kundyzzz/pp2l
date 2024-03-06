import os

def ldirfiles(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def lalldirfiles(path):
    print("All Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":
    sp = input("Enter the specified path: ")

    print("\nListing directories and files in the specified path:")
    ldirfiles(sp)

    print("\nListing all directories and files in the specified path:")
    lalldirfiles(sp)