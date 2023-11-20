import math

def calculate_square_root(number):
    square_root = math.sqrt(number)
    return square_root

# Example usage:
number = float(input("Enter a number: "))  # Take input from the user
if number >= 0:  # Check if the number is non-negative1
    result = calculate_square_root(number)
    print(f"The square root of {number} is {result:.2f}")
else:
    print("Please enter a non-negative number.")
