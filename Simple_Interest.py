#Python Program for simple interest

# Define a function to calculate simple interest
def simple_interest(p, r, t):
    '''SI = P × R × T / 100 
    where SI = simple interest, P = principal amount,
    R = the interest rate per annum, and T = the time in years.'''
    # Calculate simple interest using the formula: SI = P * (R/100) * T
    SI = p * (r / 100) * t

    # Print the calculated simple interest
    print(' Simple Interest = ', SI)

# Prompt the user to input the principal amount, interest rate, and time period
principal = int(input('Enter the Principal amount:  Rs'))
interest_rate = float(input('Enter the interest Rate per annum (in %): '))
time_period = int(input('Time period (years):  '))

# Call the simple_interest function with the provided inputs
simple_interest(principal, interest_rate, time_period)



