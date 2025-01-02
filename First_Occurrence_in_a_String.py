# the Index of the First Occurrence in a String


haystack = "mississippi"
needle = "issip"

# Check if 'needle' is a substring of 'haystack'
if needle in haystack:
    # Find the starting index of the first occurrence of 'needle' in 'haystack'
    ind = haystack.find(needle)
    # Print the index where 'needle' starts in 'haystack'
    print(ind)

      

