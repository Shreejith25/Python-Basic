# Python program to print all even numbers in a range

'''
Step 1: get in put from user for start and end range

Step 2 create empty list 

Step3 use for loop as range (strat and end)

Step 4 check each number if they are even or not

Step 5 if even appens in empty list '''

# Define a function to generate a list of even numbers within a specified range
def even(start, end):
    """
    This function generates a list of even numbers within a specified range.

    Parameters:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        list: A list containing even numbers within the specified range.
    """
    even = []

    # Iterate through each number in the range
    for i in range(start, end + 1):
        # Check if the number is even
        if i % 2 == 0:
            # Append the even number to the 'even' list
            even.append(i)

    # Return the list of even numbers
    return even


# Prompt the user to input the start and end of the range
s = int(input('Enter start of the list: '))
e = int(input('End of the list: '))

# Call the function to generate the list of even numbers and print the result
print(f'Even elements between range {s} , {e} are:', even(s, e))
