def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    upper_count, lower_count = count_upper_lower(user_input)
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")