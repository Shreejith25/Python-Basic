#Check if a Substring is Present in a Given String

'''
Step 1: Get input string and substring
Step 2: check if substring is in string using if else and in fuction
Step 3: result output '''

# Prompt the user to enter a string
string = input("Enter a string: ")

# Prompt the user to enter a substring to check
substring = input("Enter the substring to check: ")

# Check if the substring is present in the given string using the 'in' keyword
if substring in string:
    # If the substring is present, print a message indicating its presence
    print("Substring is present in the given string.")
else:
    
    # If the substring is not present, print a message indicating its absence
    print("Substring is not present in the given string.")
