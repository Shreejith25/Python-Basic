#Python program to find second largest number in a list

# Defining a list of integers
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Converting the list to a string for display purposes
actual = str(lst)

# Sorting the list in descending order using bubble sort algorithm
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]



# Displaying the second largest element in the original list
print(f'Second Largest in the List {actual} is:', lst[1])
