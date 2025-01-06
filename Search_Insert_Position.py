'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
'''



# Function to find the position to insert the target in a sorted list
def search_insert(nums, target):
    # Check if the target is already in the list
    if target in nums:
        # If target is found, get its index
        output = nums.index(target)
    else:
        # If target is not in the list:
        # Add the target to the list
        nums.append(target)
        # Sort the list to maintain order
        nums.sort()
        # Get the index of the target after sorting
        output = nums.index(target)
    
    # Print the output index
    print(output)


# Input list and target value
nums = [1, 3, 5, 6]  # A sorted list of numbers
target = 4  # The value to search for or insert

# Call the function to find the insert position or index
search_insert(nums, target)
