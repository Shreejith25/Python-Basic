# Python program to find sum of elements in list

''' 
Step 1  set sum as 0
Step 2 using for loop Iterate  each of the elements
Step 3 add the elements into sum and save it in sum 
Step 4 print the sum varaible'''


lst = [2, 3, 5, 6, 7,10]

# Initialize a variable 'sum' to keep track of the total sum
sum = 0

# Iterate through each element (i) in the list 'lst'
for i in lst:
    # Add the current element to the sum
    sum += i

# Print the total sum of all elements in the list
print(f'Total Sum of all elements in the list {str(lst)} = ', sum)

