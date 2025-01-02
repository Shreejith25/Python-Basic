#  Words Frequency in String Shorthands

'''
Step1 : split thei string
Step 2 : use for loop to get each word 
Step 3 : set count as 0
Step 4 : use for loop to get words from the list to compare
Step 5: if i and j are same add 1 to count
strp 6: Print the word and count'''

# Define the input string
input_str = 'my dear wrong number'

# Split the input string into a list of words
lst = input_str.split()

# Iterate through each word in the list
for i in lst:
    count = 0
   
    # Count the frequency of the current word in the list
    for j in lst:
        if i == j:
            count+=1
    
    # Print the word and its frequency
    print(f'Word Frequency for word - {i} -: {count}')

