#Multiply all numbers in the list

'''
Step 1 Intialize Product variable as 1
Step 2 Using Loop Iterate  each elements from the list
Step 3 Multiply each element in the list with product variable
Step 4 Print Product variable'''

lst = [2, 3, 5, 6, 7]

# Initialize a variable 'prod' to keep track of the total product
prod = 1

# Iterate through each element (i) in the list 'lst'
for i in lst:
    # Multiply the current element to the running product
    prod *= i

# Print the total product of all elements in the list
print(f'Total Product of all elements in the list {str(lst)} = ', prod)
