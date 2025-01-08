digit = [4, 3, 2, 1]

def plus_one(in_list: list) -> list:
    # Combine the digits into a single number by converting them to strings and joining them.
    num = int(''.join(map(str, in_list)))
    
    # Add 1 to the number.
    num += 1
    
    # Break the new number back into a list of digits.
    return list(map(int, str(num)))

# Test the function.
print(plus_one(digit))
