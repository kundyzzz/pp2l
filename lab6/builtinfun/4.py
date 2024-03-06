import time
import math

def square_root_after_milliseconds(milliseconds):
    time.sleep(milliseconds / 1000) 
    number = float(input("Enter a number to calculate its square root: "))
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

if __name__ == "__main__":
    milliseconds = int(input("Enter the number of milliseconds to wait: "))
    square_root_after_milliseconds(milliseconds)