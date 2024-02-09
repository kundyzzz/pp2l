def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Prime", filter_prime(numbers))