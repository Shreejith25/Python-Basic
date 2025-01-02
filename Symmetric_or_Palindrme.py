# Python program to check whether the string is Symmetrical or Palindrome

def string_operation(data):
    """
    This function performs string operations to check for symmetry and palindrome properties.

    Parameters:
        data (str): The input string to be checked.

    Returns:
        None

    Prints:
        Messages indicating whether the input string is a palindrome and/or symmetrical.
    """
    # Check if the input string is a palindrome
    if data == data[::-1]:  
         print(f'{data} is Palindrome')
    else:
         print(f'{data} is not Palindrome')

    # Check if the input string can be divided into equal halves
    if len(data) % 2 != 0:  
        # If the length is not even, the string cannot be divided symmetrically
        print(f"Can't be divided, So {data} is Not Symmetrical")
    else:
        # If the length is odd, split the string into two halves and compare them
        if data[:int(len(data)/2)] == data[int(len(data)/2)+1:][::-1]: 
            print(f'{data} is Symmetrical')
        else:
            print(f'{data} is not Symmetrical')



inp = input('Enter the String: ')
string_operation(inp)
