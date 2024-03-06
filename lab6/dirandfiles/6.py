import os
import string
def generate_alphabet_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            file.write(f"This is the file for letter {letter}.\n")
    print(f"Generated 26 text files named A.txt, B.txt, ..., Z.txt in '{directory}'.")

if __name__ == "__main__":
    directory = "alphabet_files"
    generate_alphabet_files(directory)