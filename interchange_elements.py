# Input list
lst = [12, 23, 4, 3, 4, 15, 32]

# Swap the first and last elements using simultaneous assignment
# The syntax lst[0], lst[-1] = lst[-1], lst[0] swaps the values of the first and last elements
lst[0], lst[-1] = lst[-1], lst[0]

# Print the list after swapping
print(lst)