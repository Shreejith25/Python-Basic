from operator import contains


def Armstrong(num):

    """
    Check if a given number is an Armstrong number.

    Parameters:
    - num (str): The input number as a string.

    Prints a message indicating whether the input number is an Armstrong number or not.
    """

    # Check if the input contains only numeric characters
    if not num.isdigit():
        print('Error: Input should contain only numeric characters.')
        return
    # Calculate the length of the input number
    length = len(num)

    # Initialize the sum variable
    total_sum = 0

    

    # Iterate through each digit in the number
    for digit in num:
        # Convert the digit to an integer
        digit_int = int(digit)
        
        # Calculate the power of the digit based on the length
        digit_power = digit_int ** length
        
        # Add the result to the total sum
        total_sum += digit_power

    # Check if the total sum is equal to the original number
    if total_sum == int(num):
        print(f'{num} is an Armstrong number')
    else:
        print(f'{num} is not an Armstrong number')

# Get user input for the number as string
num = input('Enter the number: ')

# Call the Armstrong function with the input number
Armstrong(num)
