#Python Program for factorial of a number


# Prompt the user to enter a number and convert it to an integer
num = int(input('Enter the Number: '))

# Create the variable 'prod' to store the product of factorials
prod = 1

# Loop through numbers from 1 to 'num' (including num)
for i in range(1, num + 1):
    # Calculate the product of factorials
    prod = prod * i

# Print the factorial of the entered number
print(f'Factorial of {num} : ', prod)



