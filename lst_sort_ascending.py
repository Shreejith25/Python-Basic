# Input list
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]



# Outer loop to iterate through each element in the list
for i in range(len(lst)):
    # Inner loop to compare the current element with the rest of the elements
    for j in range(i + 1, len(lst)):
        # Check if the current element is greater than the next element
        if lst[i] > lst[j]:
            # Swap the elements if the condition is true
            lst[i], lst[j] = lst[j], lst[i]

    

# Print the sorted list
print(lst)

            
            
    

    