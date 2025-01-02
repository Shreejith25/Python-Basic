# Python program to check if a string is palindrome or not
'''
Step1 : input as string
Step2 : using slicing inverse the string
Step3 : compare the input and inverse 
Step4 : output  palindrome or not'''


def Palindrome(inp):
    """
    This function checks if a given string is a palindrome or not.

    Parameters:
        inp (str): The input string to be checked.

    Returns:
        None

    Prints:
        A message indicating whether the input string is a palindrome or not.
    """
    # Check if the input string is equal to its reverse
    if inp == inp[::-1]:
        # If the string is equal to its reverse, it is a palindrome
        print(f'String {inp} is Palindrome')
    else:
        # If the string is not equal to its reverse, it is not a palindrome
        print(f'String {inp} is Not a Palindrome')


# Prompt the user to input a string
inp = input('Enter the String: ')

# Call the Palindrome function to check if the input string is a palindrome
Palindrome(inp)



