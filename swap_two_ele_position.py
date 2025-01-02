#take Input two positions (pos1 and pos2) in the list to swap numbers.
# check input positions are valid (between 1 and the length of the list).
# if yes, swap the numbers at those positions; 
# if no then  Invalid Input


# Input list
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Get user input for the positions to be swapped
pos1 = int(input('Enter First Element Position: '))
pos2 = int(input('Enter Second Element Position: '))
print(len(lst))
# Check if the entered positions are valid indices in the list
if 1 <= pos1 <= len(lst) and 1 <= pos2 <= len(lst):
    # Swap the elements at the specified positions using simultaneous assignment
    lst[pos1 - 1], lst[pos2 - 1] = lst[pos2 - 1], lst[pos1 - 1]
else:
    # Print an error message for invalid input positions
    print('Invalid Input')

# Print the list after the swap 
print(lst)




