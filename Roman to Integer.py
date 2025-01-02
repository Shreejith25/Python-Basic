s = "IV"  # Example Roman numeral string
roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0  # Initialize total to store the integer value
prev_value = 0  # Initialize prev_value to keep track of the previous value

# Iterate through the Roman numeral string in reverse order
for numeral in s[::-1]:
    current_value = roman_values[numeral]  # Get the integer value of the current Roman numeral

    # Check if the current value is greater than or equal to the previous value
    if current_value >= prev_value:
        total += current_value  # Add the current value to the total
    else:
        total -= current_value  # Subtract the current value from the total

    prev_value = current_value  # Update prev_value for the next iteration

print(total)  # Print the final integer value
