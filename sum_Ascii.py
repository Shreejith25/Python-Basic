# Prompting the user to enter a string
str1 = input('Enter the string: ')

# Initializing the sum variable to store the sum of ASCII values
sum = 0

# Iterating through each character in the string
for i in str1:
    # Calculating the ASCII value of the current character
    as_val = ord(i)
    # Adding the ASCII value to the sum
    sum += as_val

# Displaying the sum of ASCII values for the entered string
print(f'Sum of ASCII for {str1}:', sum)

    
