# Python program to print even length words in a string

'''
Step1 : split the string words
Step2 : use for loop to select each words
Step3: convert each ele into string 
Step4  use for loop to check even off
Step5 : if even append into empty list
Step6:  join the new List using join function'''


# Define the input string
s = "This is a python language"

# Initialize an empty list to store words with even letters
new = []

# Split the string into words
lst = s.split()

# Iterate through each word in the list
for i in lst:
    # Calculate the length of the word
    letter = len(str(i))
    
    # Check if the length of the word is even
    if (letter % 2 == 0):
        # If the length is even, append the word to the 'new' list
        new.append(i) 
    
# Join the words with even letters back into a string
new_str = " ".join(new)

# Print the resulting string
print(f'String with even letters: {new_str}')

    

    