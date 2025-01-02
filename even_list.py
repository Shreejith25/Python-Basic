# Python program to print even numbers in a list

'''
Step1: create an empty list 
Step2: create the for loop to select the selecting elach elements
Step3: check the element if element is even
Step4: if yes the append in empty element

'''

# Define a list of integers
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Initialize an empty list to store even elements
even = []

# Iterate through each element in the list
for i in lst:
    # Check if the element is even
    if i % 2 == 0:
        # Append the even element to the 'even' list
        even.append(i)

# Print the list of even elements along with the original list
print(f'List of even elements in {str(lst)}:', even)


