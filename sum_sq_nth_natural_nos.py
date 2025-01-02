# Initialize the value of n
n = 4

# Initialize the variable to store the sum
sum = 0

# While n is greater than 0, repeat the following block of code
while n > 0:
    # Add the square of the current value of n to the sum
    sum += (n ** 2)
    
    # Decrease the value of n by 1 in each iteration
    n -= 1

# Print the final sum after the loop completes
print(sum)
