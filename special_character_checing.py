#Program to check if a string contains any special character

'''
Step1 : define special characters 
Step2 :  get input from user
Step3 : use for loop to select each letter from input str
Step4: check if letter is in speacial characters
'''
# Define special characters
special_characters = "!@#$%^&*()_+{}[];:'\"<>,.?/\\|-"

# Prompt the user to enter a string
in_str = input('Enter the string: ')

# Iterate through each character in the input string
for i in in_str:
    # Check if the character is in the set of special characters
    if i in special_characters:
        # If a special character is found, print a message and break out of the loop
        print(f'String {in_str} contains special characters')
        break
else:
    # If no special character is found, print a message
    print(f'String {in_str} does not contain special characters')

