#Python Program to Accept the Strings Which Contains all Vowels

def check_vowels(in_str):
    """
    Check if a string contains all vowels (a, e, i, o, u).

    Parameters:
        in_str (str): The input string to check.

    
    """
    if ('a' in in_str and 'e' in in_str and 'i' in in_str and 'o' in in_str and 'u' in in_str):
        a = print('Accepted')
    else:
        a = print('Not accepted')
    return a

# Define the input string
str1 = 'Hello how are you'

# Call the function to check if the input string contains all vowels
check_vowels(str1)
