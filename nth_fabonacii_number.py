# Get input from the user and convert it to an integer
n = int(input('Enter the value: '))

# Check if the input is less than or equal to 1
if n <= 1:
    print('Error: Input correct value')
else:
    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1

    # Loop to calculate Fibonacci sequence up to the specified value of n
    for i in range(2, n + 1):
        # Update values of a and b using tuple unpacking
        a, b = b, a + b

        # Print each Fibonacci number in the sequence
        print(a)

    # Print the final result after the loop completes
    print(f"The {n}th Fibonacci number is: {b}")
