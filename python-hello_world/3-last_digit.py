
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
status = ""

if last_digit > 5:
    status = "greater than 5"
elif last_digit == 0:
    status = "0"
else:
    status = "less than 6 and not 0"

print("Last digit of", number, "is", last_digit, "and is", status)
