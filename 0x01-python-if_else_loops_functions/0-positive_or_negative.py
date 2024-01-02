#!/usr/bin/python3
import random

number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    result = "is positive"
elif number == 0:
    result = "is zero"
else:
    result = "is negative"

# Print the generated number and result
print(f"{number} {result}")
