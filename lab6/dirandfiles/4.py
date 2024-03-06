def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = sum(1 for line in file)
        print(f"The file '{file_path}' contains {lines} lines.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    count_lines_in_file(file_path)