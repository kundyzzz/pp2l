import os
def delete_file_if_possible(file_path):
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    if not os.access(file_path, os.W_OK):
        print(f"The file '{file_path}' is not writable (permission denied).")
        return
    try:
        os.remove(file_path)
        print(f"The file '{file_path}' has been successfully deleted.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")
if __name__ == "__main__":
    specified_path = input("Enter the path of the file to be deleted: ")
    delete_file_if_possible(specified_path)