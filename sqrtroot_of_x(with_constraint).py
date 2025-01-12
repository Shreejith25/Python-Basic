








from math import sqrt

def sqrtroot_of_(num: int) -> int:
    # Check if the number is within the valid range
    if 0 <= num <= (2**31) - 1:
        try:
            # Calculate the square root and convert it to an integer
            return int(sqrt(num))
        except ValueError:
            print("The number should be a non-negative integer")
            return -1  # Return a default value to indicate an error
    else:
        print("The number should be between 0 and 2^31-1")
        return -1  # Return a default value to indicate an error

# Prompt user to input a number
x = int(input("Enter the number: "))

# Print the square root of the user input number using the sqrtroot_of_ function
result = sqrtroot_of_(x)
if result != -1:
    print(f"Square Root of {x} is {result}")
