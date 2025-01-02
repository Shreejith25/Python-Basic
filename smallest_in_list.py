#Python program to find smallest number in a list


'''
Step 1: create outer loop to select the first element of the list using index
Step 2 :Create a second loop to select each elements after the initial element using index
Step 3: CHeck if the element is bigger than the reset of the elements if no then interchange the index of the elememnts
Step 4: Select the element index 0 of thelist for the output and print it'''

# Defining a list of integers
lst = [2, 44, 3, 5, 6, 88, 9, 1, 3, 5]

# Converting the list to a string for display purposes
actual = str(lst)

# Sorting the list in ascending order using bubble sort algorithm
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

# Displaying the sorted list
print(lst)

# Displaying the least element in the original list
print(f'Least in the List {actual} is:', lst[0])