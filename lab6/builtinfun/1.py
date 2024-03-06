from functools import reduce

def multiply_list_numbers(lst):
    result = reduce(lambda x, y: x*y, lst)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
result = multiply_list_numbers(numbers)
print(f"The result of multiplying all the numbers in the list {numbers} is: {result}")