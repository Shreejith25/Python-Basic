# Find Initial and Final Indices of Target Value in List
'''
Step 1 Sort using srt function 
Step 2 Using index Function find index of first index of traget
Step 3 Using count function find the occurance of traget
Step 4 final index first index +count -1'''

lst = [1,2,3,5,4,6,12,7,8,9,12,6,6,10]  # Given list
target = 3  # Target value to search for

# Define function to find initial and final indices of the target value in the list
def indices(lst, target):
    lst.sort()  # Sort the list
    if target in lst:  # Check if target is in the list
        initial = lst.index(target)  # Find the index of the first occurrence of the target
        count1 = lst.count(target)  # Count the number of occurrences of the target
        final = initial + count1 - 1  # Calculate the index of the last occurrence of the target
        return [initial, final]  # Return the initial and final indices
    else:
        return [-1, -1]  # Return [-1, -1] if target is not in the list

# Call the function and print the result
print(f'Initial and final index of {target} : ', indices(lst, target))


