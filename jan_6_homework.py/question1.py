'''
1 Randomly generate 10 integers
   and return the minimum
    and maximum numbers
'''

import random            # Allows us to generate random numbers

# Generate the first random number
num = random.randint(1, 100)

# Set both minimum and maximum to the first number
# This gives us a starting point for comparisons
minimum = num
maximum = num

# Loop 9 more times so we have 10 numbers total
for i in range(9):

    # Generate another random number
    num = random.randint(1, 100)

    # If the new number is smaller than the current minimum,
    # update the minimum
    if num < minimum:
        minimum = num

    # If the new number is larger than the current maximum,
    # update the maximum
    if num > maximum:
        maximum = num

# Output the final minimum and maximum values
print(minimum, maximum)