'''
58. Length of Last Word
Easy
Topics
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.'''


# Define the function to find the length of the last word in a given string
def lengthOfLastWord(s: str) -> int:     
    # Split the string into a list of words using spaces as separators
    splited = list(s.split(sep=' '))

    # Initialize a counter to traverse the list from the end
    i = -1

    # Use a while loop to handle cases where trailing spaces create empty strings
    while len(splited[i]) == 0:  # Check if the current element is an empty string
        if len(splited[i]) == 0:  # If it's an empty string, print it (for debugging)
            print(splited[i])  
            i -= 1  # Move to the previous element

    # Once a non-empty word is found, print the result
    print(f"The last word is {splited[i]} with length {len(splited[i])}")

# Test the function with the example string
input_string = "   fly me   to   the moon  "
lengthOfLastWord(input_string )




