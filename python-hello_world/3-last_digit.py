# Importing necessary module
import random

# Assigning a random signed number to the variable number
number = random.randint(-10000, 10000)

# Printing the assigned number
print(f'The string Last digit of {number} is {str(number)[-1]}', end=' ')

# Extracting the last digit of the number
last_digit = int(str(number)[-1])

# Checking whether the last digit is greater than 5, equal to 0, or less than 6 and not 0
if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print(f'and is less than 6 and not 0')
