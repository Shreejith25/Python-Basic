#Count the Number of matching characters in a pair of string

'''
Step1:  create empty list
Step2: get inputs of 2 strings
Step3: using for loop select letters from 1st string i
Step4: add inner loop for selecting letters from 2nd string j
step5: Check if i == for any value of j
step6: append to empty list if yes
Step7: Print the list and lenght of the list
'''

# Define the first string
str1 = 'abdced'

# Define the second string
str2 = 'asdechy'

# Initialize an empty list to store matching pairs
result = []

# Iterate through each character in the first string
for i in str1:
    # Iterate through each character in the second string
    for j in str2:
        # Check if the characters match
        if i == j:
            # If the characters match, append them to the 'result' list
            result.append(i)
        

# Print the matching pairs
print('Matching pairs:', result)

# Print the number of matching pairs
print('Number of matching pairs:', len(result))
