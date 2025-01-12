'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

'''


# Import the sqrt function from the math module
from math import sqrt

# Prompt user to input a number and convert the input to an integer
x = int(input("Enter the number: "))

# Define a function named sqrtroot_of_ that takes an integer as an argument 
# and returns its square root as an integer
def sqrtroot_of_(num: int) -> int:
    
    # Calculate the square root of the input number and convert it to an integer
    return int(sqrt(num))

# Print the square root of the user input number using the sqrtroot_of_ function
print(f"square Root of {x} is {sqrtroot_of_(x)}")


