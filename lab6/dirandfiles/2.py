import os

def check_access(path):
    if os.path.exists(path):
        print(f"'{path}' exists.")
    else:
        print(f"'{path}' does not exist.")
        return 
    if os.access(path, os.R_OK):
        print(f"'{path}' is readable.")
    else:
        print(f"'{path}' is not readable.")
    if os.access(path, os.W_OK):
        print(f"'{path}' is writable.")
    else:
        print(f"'{path}' is not writable.")
    if os.access(path, os.X_OK):
        print(f"'{path}' is executable.")
    else:
        print(f"'{path}' is not executable.")

if __name__ == "__main__":
    specified_path = input("Enter the specified path: ")
    check_access(specified_path)