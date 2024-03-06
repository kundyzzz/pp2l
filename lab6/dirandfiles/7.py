def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as source_file, \
             open(destination_path, 'w', encoding='utf-8') as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"Contents copied from {source_path} to {destination_path}.")
    except FileNotFoundError:
        print("The source file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_path = input("Enter the source file path: ")
    destination_path = input("Enter the destination file path: ")
    copy_file(source_path, destination_path)