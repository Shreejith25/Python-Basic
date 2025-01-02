#Python program to find N largest elements from a list

# Define a list of integers
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Define a function to find the nth largest element in the list
def n_large(n):
    """
    This function finds the nth largest element in a given list.
    
    Parameters:
        n (int): The index of the element to find, where 0 corresponds to the largest element, 
                 1 corresponds to the second largest, and so on.
    
    Returns:
        None
    
    Prints:
        The nth largest element in the list along with a message indicating its position.
    """
    # Convert the list to a string for display purposes
    actual = str(lst)
    # Check if the input index is valid
    if n >= int(len(lst)):
        print('Invalid index')
    else:
        # Sort the list in descending order using bubble sort algorithm
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        # Print the nth largest element in the list
        print(f'Least in the List {actual} is:', lst[n])

# Prompt the user to input the index of the element
n = int(input('Enter the index of element: '))

# Call the function to find the nth largest element
n_large(n)






