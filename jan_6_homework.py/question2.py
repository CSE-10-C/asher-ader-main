
'''
2. Accumulator pattern using
an if statement to find
minimum and maximum
'''

# List of numbers to examine
numbers = [5, 2, 9, 1, 7]

# Start both accumulators at the first value in the list
minimum = numbers[0]
maximum = numbers[0]

# Loop through each number in the list
for num in numbers:

    # Check if the current number is smaller than the minimum
    if num < minimum:
        minimum = num

    # Check if the current number is larger than the maximum
    if num > maximum:
        maximum = num

# Output the minimum and maximum found
print(minimum, maximum)