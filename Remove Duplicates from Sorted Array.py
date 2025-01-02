# Given array nums with duplicates
nums = [1, 1, 2, 2, 3, 4, 4, 5]

# Define a function to remove duplicates from nums
def remove(nums):
    ptr = 0  # Initialize a pointer for unique elements
    for i in range(1, len(nums)):
        # Compare current element with previous unique element
        if nums[i] != nums[ptr]:
            ptr += 1  # Move pointer to the next unique position
            nums[ptr] = nums[i]  # Update nums with the unique element

    return ptr  # Return the index of the last unique element

# Call the remove function to remove duplicates and get the index of the last unique element
ptr = remove(nums)

# Print the index of the last unique element and the array with unique elements up to index ptr
print(f" Number unique element: {ptr},List with unique elements :", nums[:ptr+1])






    


