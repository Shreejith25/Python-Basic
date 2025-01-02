# How to Remove Letters From a String in Python


def remove_letters(string, letters):
    """
    Remove specified letters from a given string.

    Parameters:
        string (str): The input string from which letters will be removed.
        letters (str): The letters to be removed from the input string.

    Returns:
        str: The input string with specified letters removed.
    """
    # Iterate through each letter in the 'letters' string
    for i in letters:
        # Replace occurrences of the current letter with an empty string in the input string
        string = string.replace(i, '')
    return string

# Prompt the user to input a string and letters to remove
input_string = input("Enter a string: ")
letters_to_remove = input("Enter letters to remove: ")

# Call the 'remove_letters' function and print the result
print('Result:', remove_letters(input_string, letters_to_remove))


