# Check if element exists in list in Python

lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

'''
Step 1 input the element from User 

Step 2 check if element is in the lst

Step 3 If yes then Print exist else print not exist'''


# Get user input for the element to be checked in the list
ele = int(input('Enter the element you want to check in the List: '))

# Check if the entered element is present in the list
if ele in lst:
    # Print a message indicating that the element exists in the list
    print(f'{ele} exists in the List')
else:
    # Print a message indicating that the element does not exist in the list
    print(f'{ele} does not exist in the List')
