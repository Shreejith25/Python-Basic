# clecing the cell using three different mentods

lst1 = [2, 3, 5, 6, 7]

lst2 =[2, 6, 5, 0, 7]

lst3 = [1, 6, 10, 0, 17]

# Print the original list lst1
print('List 1: ', lst1)

# Using clear() to empty the list
lst1.clear()

# Print the list after clearing using clear()
print('Cleared list1 using clear():', lst1)

# Print the original list lst2
print('List 2: ', lst2)

# Using del to clear the list
del lst2[:]

# Print the list after clearing using del
print('Cleared list2 using del:', lst2)

# Print the original list lst3
print('List 3: ', lst3)

# Using *= 0 to clear the list
lst3 *= 0

# Print the list after clearing using *= 0
print('Cleared list3 using *= 0:', lst3)







