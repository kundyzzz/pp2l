def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    my_list = ['apple', 'banana', 'orange', 'grape']
    file_path = input("Enter the path for the file to write the list to: ")
    write_list_to_file(file_path, my_list)