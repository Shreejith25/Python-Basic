# List of strings to find the longest common prefix from
strs = ["flower","flow","flight"]

# Check if the list is empty
if not strs:
    print("")  # Print an empty string if the list is empty
else:
    longest_pref = strs[0]  # Initialize the longest common prefix with the first string in the list
    # Iterate through the remaining strings in the list
    for i in range(1, len(strs)):
        # Continue until the longest prefix is found for the current string
        while strs[i].find(longest_pref) != 0:
            longest_pref = longest_pref[:-1]  # Remove the last character from the prefix
            # If the prefix becomes empty, no common prefix exists, so print an empty string and exit the loop
            if len(longest_pref) == 0:
                print("")
                break
    print(longest_pref)  # Print the longest common prefix found among the strings
