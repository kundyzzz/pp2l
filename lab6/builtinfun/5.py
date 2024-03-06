def all_true(tuple_of_bools):
    return all(tuple_of_bools)

if __name__ == "__main__":
    tuple_of_bools = (True, True, True, False)
    if all_true(tuple_of_bools):
        print("All elements in the tuple are True.")
    else:
        print("Not all elements in the tuple are True.")