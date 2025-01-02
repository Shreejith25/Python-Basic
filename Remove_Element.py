# Define the list nums
nums = [0, 1, 2, 2, 3, 0, 4, 2]

# Define the value to remove
val = 2

# Initialize a count variable
count = 0

# Iterate over a copy of the list nums
for i in nums[:]:
    # Check if the current element is equal to val
    if i == val:
        # If yes, remove the element from nums
        nums.remove(i)
    else:
        # If no, increment the count variable
        count += 1

# Print the count of non-removed elements and the modified nums list
print(count, nums)

