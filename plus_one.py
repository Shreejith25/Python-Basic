## 66. Plus One

'''
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
'''




digit = [4, 3, 2, 1]

def plus_one(in_list: list) -> list:
    # Convert each digit in the input list to a string for concatenation.
    temp_list = [str(i) for i in digit]
    result = []
    j = ''  # Initialize an empty string to hold the concatenated number.

    # Concatenate all string digits to form a single large number as a string.
    for i in temp_list:
        j += i
    
    # Convert the concatenated string to an integer, add 1, and then back to a string.
    new = str(int(j) + 1)
    
    # Convert each character in the new string back to an integer and append it to the result list.
    for i in new:
        result.append(int(i))

    return result  # Return the resulting list.

# Test the function by passing the 'digit' list.
print(plus_one(digit))
