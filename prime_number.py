print("Enter the number")
num = int(input())

# Check if the entered number is 0 or 1, which are not prime numbers
if num == 1 or num == 0:
    print(f'{num} is Not Prime')

elif(num == 2):
    print(f'{num} is Prime')

else:
    # Iterate through numbers from 2 to (num) to check for factors
    for i in range(2, num):
        # Check if num is divisible by i
        if num % i == 0:
            # If num is divisible, it's not a prime number
            print(f'{num} is not a prime number')
            break
        else:
            # If num is not divisible by any number in the range, it is a prime number
            print(f'{num} is a prime number')
            break


    

