#Find Pairs in List with Target Sum

# Given list of integers
lst = [2, 7, 11, 15, 3, 6,8,1]

# Target sum
target = 9

# Define function to find indices of pairs in the list that sum up to the target
def indices(lst, target):
    lst1 = []  # Initialize an empty list to store pairs of indices
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:  # Check if sum of pair equals target
                lst1.append([lst[i], lst[j]])  # If yes, append the pair to the result list
    return lst1  # Return the list of pairs

# Call the function and print the result
print(f'elements with sum is {target}: ', indices(lst, target))
