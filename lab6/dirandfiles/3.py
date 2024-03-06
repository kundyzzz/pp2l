import os

def path_details(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory = os.path.dirname(path)
        print(f"Directory portion: '{directory}'")
        filename = os.path.basename(path)
        print(f"Filename portion: '{filename}'")
    else:
        print(f"The path '{path}' does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path: ")
    path_details(specified_path)