#Find length of a string in python 


'''
Step1: get input from user
Step2: set counter as 0
Step3: use for loop to select each letter
Step4: add 1 to counter as ittration takes place '''



def length(input_str):
    """
    Calculate the length of a string excluding spaces.

    Parameters:
        input_str (str): The input string.

    Returns:
        int: The length of the string excluding spaces.
    """
    count = 0

    for i in input_str:
        if i != " ":
            count += 1
    return count

# Prompt the user to input a string
input_str = input('Enter the input String: ')

# Calculate the length of the string excluding spaces and print the result
print(f'Length of string {input_str}: {length(input_str)}')


