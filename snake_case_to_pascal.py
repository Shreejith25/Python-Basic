# Convert Snake case to Pascal case
'''
Step 1: replace _ with sapce
Step 2: Use title function to change the lower case of first letter of every word to upller case 
        and use replcce finction to remove space
Step 3: Print output'''



# Define the input string
input_str = 'We_are_here'

# Replace underscore with space
output = input_str.replace("_", " ")

# Capitalize the first letter after each space
output = output.title()

# Remove spaces between words
output = output.replace(" ", "")

print(output)
