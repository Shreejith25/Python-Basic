#Python program to print odd numbers in a List

# Define a list of integers
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Initialize an empty list to store odd elements
odd = []

# Iterate through each element in the list
for i in lst:
    # Check if the element is odd
    if i % 2 != 0:
        # Append the odd element to the 'odd' list
        odd.append(i)

# Print the list of odd elements along with the original list
print(f'List of odd elements in {str(lst)}:', odd)
